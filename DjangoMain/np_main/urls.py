from . import views
from django.urls import path
from .views import RegistrationView, AccountView, become_author
from django.contrib.auth.views import LoginView, LogoutView

from .views import category_list, subscribe_category

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Добавим главную страницу
    path('news/', views.NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('news/filter/<str:category>/', views.FilteredPostListView.as_view(), name='post-filter'),
    path('news/search/', views.SearchView.as_view(), name='post-search'),
    path('news/create/', views.create_post, {'post_type': 'news'}, name='create-news'),
    path('news/<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('news/<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),

    path('articles/', views.ArticleListView.as_view(), name='articles-list'),
    path('articles/<int:pk>/', views.PostDetailView.as_view(), name='article-detail'),
    path('articles/filter/<str:category>/', views.FilteredPostListView.as_view(), name='article-filter'),
    path('articles/search/', views.SearchView.as_view(), name='article-search'),
    path('articles/create/', views.create_post, {'post_type': 'article'}, name='create-article'),
    path('articles/<int:pk>/update/', views.PostUpdate.as_view(), name='article-update'),
    path('articles/<int:pk>/delete/', views.PostDelete.as_view(), name='article-delete'),

    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('account/', AccountView.as_view(), name='account'),
    path('become_author/', become_author, name='become_author'),

    # ------------------------------------------------------------------------------
    path('categories/', category_list, name='category_list'),
    path('subscribe/<int:category_id>/', subscribe_category, name='subscribe_category'),

]
