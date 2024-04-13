from django.shortcuts import render


def home(request):
    return render(request, "biblioteca/home.html")


def cadastrar(request):
    return render(request, "biblioteca/cadastrar.html")
