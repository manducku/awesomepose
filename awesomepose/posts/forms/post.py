from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    model = Post

    class Meta:
        model = Post
        fields = ('title', 'content')
