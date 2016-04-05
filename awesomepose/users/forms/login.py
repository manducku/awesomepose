from django import forms


class LoginForm(forms.Form):
        email = forms.EmailField(widget=forms.widgets.TextInput)
        password = forms.CharField(widget=forms.widgets.PasswordInput)

        class Meta:
            fields = ['email', 'password']
