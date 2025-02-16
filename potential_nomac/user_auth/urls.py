"""Contains the Api endpoints for User Api's"""
from django.urls import path
from . import views


urlpatterns = [
    path("auth/signup/", views.SignupView.as_view(), name="signup"),
    path("auth/login/", views.LoginView.as_view(), name="login"),
]
