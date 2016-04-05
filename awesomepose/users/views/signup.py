from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from users.forms import SignupForm
from django.contrib import messages
from django.contrib.auth import get_user_model


class SignupView(TemplateView):
    template_name = "users/signup.html"

    def post(self, request):
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.warning(request, "비밀번호가 다릅니다")

        else:
            User = get_user_model()
            user = User.objects.create(
                    email=email,
                    password=password1,
                    )
            return redirect("welcome")
