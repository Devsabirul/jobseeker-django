from django.shortcuts import render
from .models import *
def index(request):
    jobs = Job_details.objects.all()
    categorys = Categories.objects.all()
    areas = Area.objects.all()
    return render(request, 'index.html',locals())

def about(request):

    return render(request, 'about-us.html')

def category(request):

    return render(request, 'category.html')

def contact_us(request):
    
    return render(request, 'contact.html')

def price(request):

    return render(request, 'price.html')

def blog(request):
    
    return render(request, 'blog-home.html')

def elements(request):
    
    return render(request, 'elements.html')

def search(request):
    title = request.GET.get("search")
    area = request.GET.get("area")
    category = request.GET.get("category")

    print(title,area,category)
    return render(request, 'search.html')

def single(request):
    
    return render(request, 'single.html')