from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
                    "email",
                )
