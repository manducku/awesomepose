from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib import messages


class SignupView(TemplateView):
    template_name = "users/signup.html"

    def post(self, request):
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        nickname = request.POST.get("nickname")
        if password1 != password2:
            messages.warning(request, "비밀번호가 다릅니다")

        else:
            User = get_user_model()
            user = User.objects.create_user(
                    email=email,
                    password=password1,
                    nickname=nickname,
                    )
            if user:
                return redirect("welcome")
            else:
                messages.warning(request, '아이디 또는  이메일이 올바르지 않습니다. 다시 입력 부탁드립니다.')
                return redirect('sign-up')
