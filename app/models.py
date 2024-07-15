from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="images/posts/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    like_count = models.PositiveIntegerField(default=0)


class Likes(models.Model):
    post_id = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="liked_user")




