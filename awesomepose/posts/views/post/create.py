from posts.forms import PostForm

from django.views.generic import FormView, CreateView


class PostCreateView(CreateView):
    template_name = "posts/create.html"
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)
