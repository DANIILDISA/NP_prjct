from django.urls import path
from .views import PostListView, PostDetailView, FilteredPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('filter/<str:category>/', FilteredPostListView.as_view(), name='post-filter'),
]
