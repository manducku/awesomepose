from rest_framework.views import APIView
from users.models import User
from posts.models import Post
from posts.models import Like
from posts.serializers.comment import CommentListSerializer
from rest_framework.response import Response
from rest_framework import status


class LikeAPIView(APIView):

    def get(self, request, **kwargs):
        post = Post.objects.get(
                pk=self.kwargs.get('slug')
                )
        user = User.objects.get(
                pk=self.request.user.id
                )
        like = Like.objects.get(post=post, user=user)
        post_like_count = post.like_set.count()
        data = [
                {
                    "count": post_like_count
                }
                ]

        return Response(data)

    def post(self, request, **kwargs):
        pass
        data = request.data
        post = Post.objects.get(
                pk=data.get('post')
                )
        comment = post.comment_set.create(
                user=request.user,
                content=data.get('content'),
                )

        serializer = CommentListSerializer(comment)
        if CommentListSerializer(data=serializer.data):
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
