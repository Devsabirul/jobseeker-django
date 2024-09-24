from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def signup(request):
    if request.method=='POST':
        s_form=SignupForm(request.POST, request.FILES, instance=request.user)
        p_form=ProfileForm(request.POST, request.FILES, instace=request.user.Profile)
        if s_form.is_valid() and p_form.is_valid():
            s_form.save()
            p_form.save()
            return redirect('indexpage')
    else:
        s_form=SignupForm(request.POST, instance=request.user)
        p_form=ProfileForm(request.POST, instace=request.user.Profile)

    context={
        's_form':s_form,
        'p_form':p_form
    }

    return render(request,'userapp/signup.html', context)

def login(request):
    
    return render(request, 'login.html')