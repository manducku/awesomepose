from django.views.generic import TemplateView


class WelcomeView(TemplateView):
    template_name = "users/welcome.html"
