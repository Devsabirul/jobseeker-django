from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path("signup/", signup, name='registration'),
    path("login/", login, name='login'),
]