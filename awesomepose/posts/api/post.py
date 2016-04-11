from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post


class PostListAPIView(APIView):

    def get(self, request):
        posts = [post.title for post in Post.objects.all()]
        return Response(posts)
