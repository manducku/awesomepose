from django.views.generic import FormView, CreateView

from posts.models import Post


class PostCreateView(CreateView):
    model = Post
    template_name = "posts/create.html"
    fields = [
            'title',
            'content',
            'image',
            ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
