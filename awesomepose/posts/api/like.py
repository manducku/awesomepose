from rest_framework.views import APIView
from users.models import User
from posts.models import Post, Like
from posts.serializers import LikeSerializer
from rest_framework.response import Response
from rest_framework import status


class LikeAPIView(APIView):

    def get(self, request, **kwargs):
        post = Post.objects.get(
                pk=self.kwargs.get('slug')
                )
        serializer = LikeSerializer(post)

        return Response(serializer.data)

    def post(self, request, **kwargs):
        data = request.data
        post = Post.objects.get(
                pk=data.get('post')
                )
        user = User.objects.get(
                pk=self.request.user.id
                )
        like, created = Like.objects.get_or_create(post=post, user=user)
        serializer = LikeSerializer(post)
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
            data = request.data
            post = Post.objects.get(
                    pk=data.get('post')
                    )

            user = User.objects.get(
                    pk=self.request.user.id
                    )
            like = Like.objects.get(post=post, user=user)
            like.delete()
            serializer = LikeSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
