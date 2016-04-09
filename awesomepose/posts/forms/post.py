from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        widgets = {
                'image': SummernoteWidget(),
                }
        fields = ['title', 'content', 'image']
