from django.shortcuts import render
from django.http import HttpResponse


def entrar(response):
    return render(response, "users/entrar.html")


def cadastrar(response):
    return render(response, "users/cadastrar.html")


def validate_user(request):
    name = request.POST.get("name")
    document = request.POST.get("document")
    email = request.POST.get("email")
    password = request.POST.get("password")
    return HttpResponse(f"{name}{email}{document}")
