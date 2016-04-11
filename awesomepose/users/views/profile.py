from django.views.generic import ListView
from posts.models import Post


class ProfileListView(ListView):
    template_name = "users/profile.html"
    context_object_name = "posts"

    def get_queryset(self):
        user_id = self.kwargs.get('slug')
        return Post.objects.filter(user=user_id)
