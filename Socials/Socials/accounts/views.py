from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin,generic.TemplateView):
    #hi
    template_name = "home.html"
    login_url = 'account_login'
