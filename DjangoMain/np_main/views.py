from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-created_at']
    template_name = 'posts.html'
    context_object_name = 'posts'


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
