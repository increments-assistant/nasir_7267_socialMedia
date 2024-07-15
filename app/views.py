from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.serializers import PostSerializer, LikeSerializer
from app.models import Posts, Likes
from app.tasks import create_like


class PostAPIView(views.APIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data["user"] = request.user
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Created Successfully", status=status.HTTP_201_CREATED)


class LikeAPIView(views.APIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        data = request.data
        data["user"] = request.user
        serializer = LikeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        create_like(data)
        return Response("Liked", status=status.HTTP_201_CREATED)



