from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import LoginForm, SignupForm
from django.views.generic import TemplateView
from django.contrib import messages
from django.core.urlresolvers import reverse


class LoginView(TemplateView):
    template_name = "users/login.html"

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        next = request.POST.get("next") or reverse("home")
        user = authenticate(
                email=email,
                password=password,
                )

        if user:
            messages.success(request, '로그인에 성공하였습니다.')
            login(request, user)
            return redirect(next)
        messages.warning(request, '비밀번호가 틀렸습니다')
        return redirect('login')
