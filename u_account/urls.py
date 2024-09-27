from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   
    path("signup", registration, name='registration'),
    path("login", login_view, name='login'),
]