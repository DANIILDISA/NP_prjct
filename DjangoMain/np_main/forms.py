from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=1, max_length=100)
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 10:
            raise ValidationError({
                "text": "text не может быть менее 100 символов."
            })

        return cleaned_data
