from .models import Category


def subscribe_to_category(user, category_id):
    category = Category.objects.get(id=category_id)
    category.subscribers.add(user)
