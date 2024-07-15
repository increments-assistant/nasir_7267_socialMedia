from django.urls import path
from app.views import PostAPIView, LikeAPIView
urlpatterns = [
    path('posts/', PostAPIView.as_view()),
    path('like/', LikeAPIView.as_view()),
]