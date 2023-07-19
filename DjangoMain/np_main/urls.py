from django.urls import path
from .views import (
    NewsListView, ArticleListView, PostDetailView, FilteredPostListView,
    SearchView, create_post, PostUpdate, PostDelete
)
from . import views

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

]


