from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import LoginForm, SignupForm


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
