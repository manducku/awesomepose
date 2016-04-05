from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import LoginForm, SignupForm
from django.views.generic import View
from django.contrib import messages


class LoginView(View):
    def get(self, request):
        template_name = "users/login.html"

        return render(
                request,
                template_name,
                context={},
                )

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(
                email=email,
                password=password,
                )

        if user:
            messages.success(request, '로그인에 성공하였습니다.')
            login(request, user)
            return redirect(next_page_url)
        messages.warning(request, '비밀번호가 틀렸습니다')
        return redirect('login')
