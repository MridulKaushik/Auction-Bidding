from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class CustomerLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('auction:home')

class CustomerLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('auction:home')
    
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'