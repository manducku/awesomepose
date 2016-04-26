from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, Button
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)

from posts.models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "상세 리뷰"
        self.fields['product_url'].label = "구매 주소"
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.label_class = 'control-label'
        self.helper.layout = Layout(
            Field('title', css_class='form-control', placeholder="제목을 입력해 주세요"),
            Field('content', css_class='form-control', ),
            Field('product_url', css_class='form-control', placeholder="구매처의 주소를 붙여넣어 주세요"),
            FormActions(Submit('save', '저장하기', css_class='btn btn-primary'),
                        Button('cancel', 'Cancel', css_class='btn btn-default')
                        ),
        )

    class Meta:
        model = Post
        widgets = {
                'title': forms.TextInput(),
                'content': SummernoteInplaceWidget(
                    ),
                'product_url': forms.TextInput(),
                }
        fields = ['title', 'content', 'product_url']
