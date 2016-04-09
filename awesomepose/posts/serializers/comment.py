from rest_framework import serializers

from posts.models import Comment


class CommentBaseSerializer(serializers.ModelSerializer):

    username = serializers.CharField(source='user.nickname',)

    class Meta:
        model = Comment
        fields = (
                'content',
                'username',
                )


class CommentListSerializer(CommentBaseSerializer):
    pass
