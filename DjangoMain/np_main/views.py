from .forms import PostForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from .models import Post, Author
from .filters import PostFilter
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test


class NewsListView(ListView):
    model = Post
    ordering = ['-created_at']
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 3
    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(post_type=Post.NEWS)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticleListView(ListView):
    model = Post
    ordering = ['-created_at']
    template_name = 'articles.html'
    context_object_name = 'posts'
    paginate_by = 3
    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(post_type=Post.ARTICLE)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class FilteredPostListView(ListView):
    model = Post
    template_name = 'filtered_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = self.kwargs['category']
        return Post.objects.filter(categories__name=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context


class SearchView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        filterset = PostFilter(self.request.GET, queryset=queryset)
        return filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


@login_required(login_url='login')
def create_post(request, post_type):
    if not request.user.groups.filter(name='authors').exists():
        return redirect('account')
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            author = Author.objects.get(user=request.user)
            post.author = author

            post_type = post_type.lower()
            if post_type == 'news':
                post.post_type = Post.NEWS
            elif post_type == 'article':
                post.post_type = Post.ARTICLE

            post.save()
            if post_type == 'article':
                return redirect('/articles/')
            else:
                return redirect(f'/{post_type}/')

    return render(request, 'post_edit.html', {'form': form})


@login_required
def become_author(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    authors_group.user_set.add(user)
    return redirect('account')


def is_author(user):
    return user.groups.filter(name='authors').exists()


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(user_passes_test(is_author), name='dispatch')
class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_success_url(self):
        post_type = self.object.post_type

        if post_type == 'article':
            return reverse('articles-list')
        elif post_type == 'news':
            return reverse('news-list')
        else:
            return None


@method_decorator(login_required(login_url='login'), name='dispatch')
@method_decorator(user_passes_test(is_author), name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'

    def get_success_url(self):
        post_type = self.object.post_type
        return reverse(f'{post_type}-list')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greeting'] = 'Добро пожаловать на главную страницу!'
        return context


class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        group = Group.objects.get(name='common')
        self.object.groups.add(group)
        return response


class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['username'] = user.username
        context['is_author'] = user.groups.filter(name='authors').exists()
        return context
