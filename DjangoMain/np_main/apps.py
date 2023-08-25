from django.apps import AppConfig
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timedelta
from .models import Post, Category, WeeklySummary


class NpMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'np_main'

    def ready(self):
        super().ready()
        self.start_weekly_newsletter_task()

    @staticmethod
    @shared_task
    def send_weekly_post_summary():  # создаём задачу для celery
        end_date = datetime.now()
        start_date = end_date - timedelta(days=end_date.weekday() + 7)
        posts = Post.objects.filter(created_at__range=[start_date, end_date])
        # тут вычисляются даты начала и
        # окончания прошлой недели и извлекаются посты, созданные в это время

        post_urls = [f"http:/news/{post.id}/" for post in posts]

        for category in Category.objects.all():
            subscribers_emails = category.subscribers.values_list('email', flat=True)
            if subscribers_emails:
                subject = f"Weekly summary ({start_date} to {end_date})"
                message = f"Here are the new news from the past week:\n" + "\n".join(post_urls)
                send_mail(subject, message, "dennisburn", subscribers_emails, fail_silently=True)

        weekly_summary = WeeklySummary.objects.create(week_start_date=start_date)
        weekly_summary.posts.set(posts)

    def start_weekly_newsletter_task(self):
        now = datetime.now()
        if now.weekday() == 0 and now.time().hour == 8:
            self.send_weekly_post_summary.delay()
