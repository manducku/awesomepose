from django.db import models
from django.conf import settings

from posts.models import Post


class Tag(models.Model):

    name = models.TextField(
            max_length=10,
            )

    update_at = models.DateTimeField(
            auto_now_add=True,
            )

    create_at = models.DateTimeField(
            auto_now=True,
            )

    def __str__(self):
        return "#{tag}".format(
                tag=self.name
                )
