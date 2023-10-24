from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.CustomerLoginView.as_view(template_name="account/login.html"),name='login'),
    path('logout/', views.CustomerLogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]
