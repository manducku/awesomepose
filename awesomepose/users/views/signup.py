from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

from users.forms import SignupForm


def signup(request):
        if request.method == "POST":
            form = SignupForm(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect("welcome")
        else:
            form = SignupForm()
        return render(
                request,
                "users/signup.html",
                {"form": form},
                )
