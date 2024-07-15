from app.models import Likes, Posts

from celery import shared_task


@shared_task
def create_like(data):
    Likes.objects.create(post_id=data.get("post_id"), user=data.get("user"))
    post = Posts.objects.get(id=data.get("post_id"))
    post.like_count += 1
    post.save()
    return "Liked"
