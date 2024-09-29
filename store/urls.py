from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #path('admin/', admin.site.urls),
    path("", index, name='indexpage'),
    path('about_us/', about, name='about_us'),
    path('category/', category, name='category'),
    path('contact/', contact_us, name='contact_us'),
    path('price/', price, name='price_us'),
    path('blog/', blog, name='blog_us'),
    path('elements/', elements, name='elements_page'),
    path('search', search, name='search_page'),
    path('single/', single, name='single_page'),
   
]