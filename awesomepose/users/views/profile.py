from django.views.generic import DetailView
from users.models import User


class ProfileView(DetailView):
    template_name = "users/profile.html"
    model = User
    slug_field = "id"
