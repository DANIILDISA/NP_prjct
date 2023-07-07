from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'post_type', 'created_at', 'rating']
    filter_horizontal = ['categories']


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['post', 'category']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'user', 'text', 'created_at', 'rating']
