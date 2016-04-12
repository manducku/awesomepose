from django.db import models
from django.conf import settings

from posts.models import Post


class Like(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            )

    post = models.ForeignKey(
            Post,
            )

    create_at = models.DateTimeField(auto_now_add=True,)
    update_at = models.DateTimeField(auto_now=True,)
