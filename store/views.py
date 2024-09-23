from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

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
    
    return render(request, 'search.html')

def single(request):
    
    return render(request, 'single.html')