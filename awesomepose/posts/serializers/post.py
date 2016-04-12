from rest_framework import serializers

from posts.models import Post


class PostBaseSerializer(serializers.ModelSerializer):

    nickname = serializers.CharField(source='user.nickname',)
    profile_image = serializers.ImageField(source='user.profile_image',)

    class Meta:
        model = Post
        fields = (
                'nickname',
                'profile_image',
                'title',
                'content',
                )


class PostListSerializer(PostBaseSerializer):
    pass
