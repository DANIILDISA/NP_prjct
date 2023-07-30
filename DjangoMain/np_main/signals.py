from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post, Category, WeeklySummary
from datetime import datetime, timedelta


@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created and instance.post_type == Post.ARTICLE:
        subscribers_emails = instance.categories.values_list('subscribers__email', flat=True)
        if subscribers_emails:
            post_url = instance.get_absolute_url()
            subject = f"New article: {instance.title}"
            message = f"A new article '{instance.title}' has been added.\n\n{instance.preview()}\n\nRead it at {post_url}."
            send_mail(subject, message, "dennisburn", subscribers_emails, fail_silently=True)


@receiver(post_save, sender=WeeklySummary)
def send_weekly_post_summary(sender, instance, created, **kwargs):
    if created:
        # Получаем начальную и конечную даты за прошедшую неделю
        end_date = datetime.now()
        start_date = end_date - timedelta(days=end_date.weekday() + 7)

        # Получаем все посты, созданные за последнюю неделю
        posts = Post.objects.filter(created_at__range=[start_date, end_date])

        # URL-адреса постов для электронной почты
        post_urls = [f"http://your_website_url/news/{post.id}/" for post in posts]

        # Рассылка еженедельной сводки всем подписчикам каждой категории
        for category in Category.objects.all():
            subscribers_emails = category.subscribers.values_list('email', flat=True)
            if subscribers_emails:
                subject = f"Weekly Article Summary ({start_date} to {end_date})"
                message = f"Here are the new articles from the past week:\n" + "\n".join(post_urls)
                send_mail(subject, message, "your_email@example.com", subscribers_emails, fail_silently=True)

        # Объект WeeklySummary для хранения сводки
        weekly_summary = WeeklySummary.objects.create(week_start_date=start_date)
        weekly_summary.posts.set(posts)
