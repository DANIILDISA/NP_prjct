from django import forms
from .models import Post
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=100)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'categories',
        ]

    # def clean_text(self):
    #     cleaned_data = super().clean()
    #     text = cleaned_data.get("text")
    #     if text is not None and len(text) < 10:
    #         raise ValidationError({
    #             "text": "text не может быть менее 100 символов."
    #         })
    #
    # def clean_categories(self):
    #     cleaned_data = super().clean()
    #     categories = cleaned_data.get("categories")
    #     # надо посчитать количество категорий и если больше 2 - выкинуть raise
    #     return cleaned_data


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
