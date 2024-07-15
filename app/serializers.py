from rest_framework import serializers
from app.models import Posts, Likes


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
