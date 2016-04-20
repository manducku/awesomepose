from rest_framework import serializers

from posts.models import Like, Post
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
                'id',
                'email',
                'nickname',
                )


class LikeSerializer(serializers.ModelSerializer):

    like_user_set = UserSerializer(many=True)

    class Meta:
        model = Post
        fields = (
                'like_user_set',
                )
