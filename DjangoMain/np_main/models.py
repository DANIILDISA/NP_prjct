from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def calculate_rating(self):
        pass

    def __str__(self):
        return self.user.username  # type: ignore

    def update_rating(self):
        article_rating = self.post_set.aggregate(Sum('rating'))['rating__sum'] or 0  # type: ignore
        comment_rating = Comment.objects.filter(post__author=self).aggregate(Sum('rating'))[
                             'rating__sum'] or 0  # type: ignore
        article_comment_rating = Comment.objects.filter(post__author=self).aggregate(Sum('rating'))[
                                     'rating__sum'] or 0  # type: ignore

        self.rating = article_rating * 3 + comment_rating + article_comment_rating
        self.save()


class Post(models.Model):
    ARTICLE = 'article'
    NEWS = 'news'
    POST_TYPES = [
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость'),
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=10, choices=POST_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    content = models.TextField()

    def calculate_rating(self):
        pass

    def __str__(self):
        return self.title

    # def like(self):
    #     self.rating += 1  # type: ignore
    #     self.save()
    #
    # def dislike(self):
    #     self.rating -= 1  # type: ignore
    #     self.save()

    def preview(self):
        preview_length = 124
        if len(self.text) > preview_length:  # type: ignore
            return self.text[:preview_length] + '...'
        else:
            return self.text

    def get_absolute_url(self):
        return reverse('PostDetailView', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} - {self.category}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    # def like(self):
    #     self.rating += 1
    #     self.save()
    #
    # def dislike(self):
    #     self.rating -= 1
    #     self.save()
    #

    def __str__(self):
        return self.text
