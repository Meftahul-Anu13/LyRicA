from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request) :
    # return HttpResponse("Lyrica is a music player website!")
    # context = {}
    # template = 'home/home.html'
    # return render(request, template, context)
    return render(request , 'login.html')
