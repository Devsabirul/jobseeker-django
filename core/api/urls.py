from django.urls import path 
from .views import *

urlpatterns = [
    path("welcome",Startproject.as_view())
]
