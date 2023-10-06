# from django.core.mail import send_mail
# from .models import Post
# from celery import shared_task
#
#
# @shared_task
# def send_post_notification(post_id):  # создаём задачу для celery
#     try:
#         post = Post.objects.get(pk=post_id)
#         if post.post_type == Post.NEWS:
#             subscribers_emails = post.categories.values_list('subscribers__email', flat=True)
#             if subscribers_emails:
#                 post_url = post.get_absolute_url()
#                 subject = f"New post: {post.title}"
#                 message = f"A new post '{post.title}' has been added.\n\n{post.preview()}\n\nRead it at {post_url}."
#                 send_mail(subject, message, "dennisburn", subscribers_emails, fail_silently=True)
#     except Post.DoesNotExist:
#         pass
