
from django.urls import path
from django.contrib.auth import views as auth_views

from demo.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('validate_username', validate_username, name='validate_username'),

    path('about', about, name='about'),
    path('application', application, name='application')



]
