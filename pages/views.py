from django.shortcuts import render
from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello, World")

def HelloWord(request):

    return render(request, 'hello_word.html')