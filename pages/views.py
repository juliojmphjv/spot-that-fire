from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, World")

def home(request):

    return render(request, 'index.html')

def boilerplate(request):

    return render(request, 'boilerplate.html')

def whats_signup(request):

    return render(request, 'qrcode.html')