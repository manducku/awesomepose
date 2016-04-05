from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import LoginForm, SignupForm
from django.views.generic import View


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
            login(request, user)
            return redirect(next_page_url)

        return redirect('login')


"""
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(email=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    (request, user)
                    return redirect('welcome')
    else:
        form = LoginForm()

    return render(
            request,
            'users/login.html',
            {
                'form': form,
            }
          )
"""
