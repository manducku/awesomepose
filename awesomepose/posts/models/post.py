from django.db import models
from django.conf import settings

from tags.models import Tag


class Post(models.Model):

    user = models.ForeignKey(
            settings.AUTH_USER_MODEL
            )

    image = models.ImageField()
    title = models.TextField(max_length=20)
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

    # post_set과 이름이 겹치므로, like_user_set으로 이름 생성
    like_user_set = models.ManyToManyField(
            settings.AUTH_USER_MODEL,
            related_name="like_post_set",
            through="Like",
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


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s".format(slug, filename)


class Images(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to=get_image_filename)
