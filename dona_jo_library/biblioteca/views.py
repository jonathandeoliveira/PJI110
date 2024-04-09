from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, "biblioteca/home.html")


def cadastrar(request):
    return HttpResponse("teste ok")
