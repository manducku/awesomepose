from django.apss import AppConfig


class PostAppConfig(AppConfig):
    name = "posts"

    def ready(self):
        from post.signals.post_save import post_save_post_tag
