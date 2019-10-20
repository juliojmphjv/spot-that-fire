from django.shortcuts import render
from django.http import HttpResponse


def home(request):

    return render(request, "index.html")


def whats_signup(request):

    return render(request, "qrcode.html")


def missao(request):

    return render(request, "missao.html")


def estatistica(request):

    return render(request, "estatistica.html")
