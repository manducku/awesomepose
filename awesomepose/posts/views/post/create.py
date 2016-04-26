from django.views.generic import FormView, CreateView
from django.forms import formset_factory, modelform_factory
from django.shortcuts import render
from bs4 import BeautifulSoup

from posts.models import Post
from posts.forms import PostForm


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = "posts/create.html"
    sucess_url = "/"

    # save image using BeautifulSoup
    def form_valid(self, form):
        form = PostForm(self.request.POST)
        if form.is_valid():
            soup = BeautifulSoup(form.instance.content, 'html.parser')
            form.instance.image = soup.img.get('src')
            form.instance.user = self.request.user
            form.save()
        return super(PostCreateView, self).form_valid(form)
