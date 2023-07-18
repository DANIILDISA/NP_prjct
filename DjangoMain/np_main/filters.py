import django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author__user__username__icontains = django_filters.CharFilter(field_name='author__user__username', lookup_expr='icontains')
    created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')

    class Meta:
        model = Post
        fields = ['title', 'author__user__username__icontains', 'created_at__gte']
