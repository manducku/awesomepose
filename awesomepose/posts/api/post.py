from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from posts.models import Post
from posts.serializers.post import PostListSerializer


class PostSetPagination(PageNumberPagination):
        page_size = 5


class PostListAPIView(ListAPIView):
        queryset = Post.objects.all()
        pagination_class = PostSetPagination
        serializer_class = PostListSerializer
