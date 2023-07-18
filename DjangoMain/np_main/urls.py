from django.urls import path
from .views import (
    NewsListView, ArticleListView, PostDetailView, FilteredPostListView,
    SearchView, create_post, PostUpdate, PostDelete
)
from . import views

urlpatterns = [

    # path('', NewsListView.as_view(), name='news-list'),
    # path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # # Если отключить эти строки, то будет сортировка по статьям.
    # # Задача такая: перенаправлять с default.html сюда, на разные urls шаблоны,
    # # проблема в том, что через spacename не получается, выдает ошибку, разобраться.
    # # Пробуй всё переписать с нуля.
    # # Например, сделать всё в тупую, через ветки, а не через подстановку, тупо всё вручную прописать,
    # # да костыль, но уже надо хоть как-то сделать.
    # path('', ArticleListView.as_view(), name='articles-list'),
    # path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # path('filter/<str:category>/', FilteredPostListView.as_view(), name='post-filter'),
    # path('search/', SearchView.as_view(), name='post-search'),
    # path('create/', create_post, name='create-post'),
    # path('<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    # path('<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),

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

"""
объясни простым языком логику работы данной схемы, правильно ли я понимаю? Вот смотри, это фрагмент файла default.html: 
(звездочками я обозначаю начало и конец кода из файлов)

*</li>
<li class="nav-item">
    <a class="nav-link" href="/news">News</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="/articles">Articles</a>*

допустим я нажал на /news
джанго после этого меня кидает сюда: 

urls.py
*urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('np_main.urls')),
    path('articles/', include('np_main.urls')),
]* 
"path('news/', include('np_main.urls'))," ссылается на приложение np_main. В нем есть свой файл urls.py: 
*urlpatterns = [

    path('', NewsListView.as_view(), name='news-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', ArticleListView.as_view(), name='articles-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('filter/<str:category>/', FilteredPostListView.as_view(), name='post-filter'),
    path('search/', SearchView.as_view(), name='post-search'),
    path('create/', create_post, name='create-post'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),

]
*
и получается вот это news/ подставляется сюда "path('', NewsListView.as_view(), name='news-list'),"
и запускается представление NewsListView.as_view(). 
И загвоздка в том, что если я нажму на /articles, то я тоже запущу NewsListView.as_view().
Вот как мне сделать так, чтобы при нажатии /articles запускалась вот эта строчка 
"path('', ArticleListView.as_view(), name='articles-list'),"

"""
