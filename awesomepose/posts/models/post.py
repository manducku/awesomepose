from django.db import models
from django.conf import settings

from tags.models import Tag


class Post(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL
            )

    image = models.ImageField()
    title = models.TextField()
    content = models.TextField()

    update_at = models.DateTimeField(
            auto_now_add=True,
            )
    create_at = models.DateTimeField(
            auto_now=True,
            )
    tag_set = models.ManyToManyField(
            Tag,
            )

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse

        return reverse(
                "detail",
                kwargs={
                    "slug": self.id,
                    }
                )

    def __str__(self):
        return self.title
