from django import forms
from users.models import User


class SignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.widgets.TextInput, label="Email")
    password1 = forms.CharField(widget=forms.widgets.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.widgets.PasswordInput,
                                label="Password (again)")
    nickname = forms.CharField(widget=forms.widgets.TextInput, label="nickname")

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'nickname']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
