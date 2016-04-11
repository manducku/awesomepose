from rest_framework.views import APIView

from posts.models import Post
from posts.serializers.comment import CommentListSerializer
from rest_framework.response import Response
from rest_framework import status


class PostCommentListAPIView(APIView):

    def get(self, request, **kwargs):
        post = Post.objects.get(
                pk=self.kwargs.get('slug')
                )
        comments = post.comment_set.all()
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, **kwargs):
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
