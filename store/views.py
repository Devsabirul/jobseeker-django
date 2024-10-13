from django.shortcuts import render
from .models import *
from django.db.models import Q

def index(request):
    jobs = Job_details.objects.order_by("-id")
    categorys = Categories.objects.all()
    areas = Area.objects.all()
    popular_jobs = Job_details.objects.all()[:5]
    top_jobs = Job_details.objects.all()[:3]
    categories = Categories.objects.all()
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

    search_value=Job_details.objects.filter(Q(title__startswith=title) | Q(area__icontains=area) | Q(category__category_title__icontains=category))
    return render(request, 'search.html', locals())

def single(request):
    
    return render(request, 'single.html')