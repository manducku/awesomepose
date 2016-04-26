from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from posts.models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "포스트 내용"
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2 control-label'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Field('title', css_class='form-control'),
            Field('content', css_class='form-control'),
            FormActions(Submit('save', 'save', css_class='btn btn-primary'))
        )

    class Meta:
        model = Post
        widgets = {
                'title': forms.TextInput(),
                'content': SummernoteInplaceWidget(),
                }
        fields = ['title', 'content']
