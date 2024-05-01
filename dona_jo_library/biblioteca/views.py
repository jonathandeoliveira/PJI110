from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from biblioteca.models import Books, Loans, Genres, Status
import traceback
from hashlib import sha256


def home(request):
    return render(request, "/home.html")

def cadastrar(request):
    return render(request, "biblioteca/cadastrar.html")


def cadastrar_livro(request):
    return render(request, "biblioteca/cadastrar-livro.html")
