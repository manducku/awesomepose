from django.views.generic import ListView
from posts.models import Post


class HomeView(ListView):
    template_name = "home.html"
    model = Post
    context_object_name = "posts"
