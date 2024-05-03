from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from biblioteca.models import Books, Loans, Genres, Status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def cadastrar(request):
    return render(request, "biblioteca/cadastrar.html")

def livros(request):
    books = Books.objects.filter(status__name='Disponivel')
    return render(request, "biblioteca/livros.html", {'books': books})


@login_required(login_url='/auth/entrar/') 
def emprestimos(request):
    # Verificar se o usuário está autenticado e tem um perfil de usuário
    if request.user.is_authenticated and hasattr(request.user, 'user_type') and request.user.user_type is not None: 
        # Verificar se o usuário é um bibliotecário
        if request.user.user_type.user_code == 1:
            return render(request, "biblioteca/emprestimos.html")
        else:
            return HttpResponse('Acesso negado: Você não é um bibliotecário.')
    else:
        # Se o usuário não estiver autenticado ou não tiver um tipo de usuário associado
        return HttpResponse('Acesso negado: Você não está autenticado ou não tem um tipo de usuário associado.')

