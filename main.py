"""
(Не обращайте внимания, остатки предыдущего задания)

cd  DjangoMain
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py startapp np_main
python manage.py shell

----------------------------------------------------
from np_main.models import *
from django.contrib.auth.models import User
----------------------------------------------------
user1 = User.objects.create_user('username1')
user2 = User.objects.create_user('username2')
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)
----------------------------------------------------
category1 = Category.objects.create(name='Sports')
category2 = Category.objects.create(name='Politics')
category3 = Category.objects.create(name='Education')
category4 = Category.objects.create(name='Technology')
----------------------------------------------------
article1 = Post.objects.create(author=author1, title='Заголовок статьи 1', text='Текст статьи 1')
article1.categories.add(category1, category2)
article2 = Post.objects.create(author=author2, title='Заголовок статьи 2', text='Текст статьи 2')
article2.categories.add(category2, category3)
news1 = Post.objects.create(author=author1, title='Заголовок новости 1', text='Текст новости 1')
news1.categories.add(category3)
----------------------------------------------------
comment1 = Comment.objects.create(post=article1, user=user1, text='Comment 1(1) для статьи 1')
comment2 = Comment.objects.create(post=article1, user=user2, text='Comment 2(2) для статьи 1')
comment3 = Comment.objects.create(post=article2, user=user1, text='Comment 1(3) для статьи 2')
comment4 = Comment.objects.create(post=news1, user=user1, text='Comment 1(4) для новости 1')
----------------------------------------------------
comment1.like()
comment1.like()
comment2.like()
comment2.dislike()
author1.update_rating()
author2.update_rating()
----------------------------------------------------
best_user = Author.objects.order_by('-rating').first().user
* print(f"Best User: {best_user.username}")
* print(f"Rating: {best_user.author.rating}")
----------------------------------------------------
best_article = Post.objects.order_by('-rating').first()
* print("Best Article:")
* print(f"Date Added: {best_article.created_at}")
* print(f"Author: {best_article.author.user.username}")
* print(f"Rating: {best_article.rating}")
* print(f"Title: {best_article.title}")
* print(f"Preview: {best_article.preview()}")
"""

# vhjzrhbnqjujdlis пароль 2
