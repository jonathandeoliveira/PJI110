from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from biblioteca.models import Books, Loans, Genres, Status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

def cadastrar(request):
    return render(request, "biblioteca/cadastrar.html")

def livros(request):
    books = Books.objects.all()
    return render(request, "biblioteca/livros.html", {'books': books})

def detalhes_livro(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if request.user.is_authenticated:
        if hasattr(request.user, 'user_type') and request.user.user_type is not None:
            if request.user.user_type.code_description == 'Bibliotecario':
                return render(request, 'biblioteca/detalhes-livro.html', {'book': book})
    return render(request, 'biblioteca/detalhes-livro.html', {'book': book})



@login_required(login_url='/auth/entrar/') 
def emprestimos(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    if book.status.name == 'Emprestado':
        return HttpResponse('Este livro já está emprestado.')
    renters = UserProfile.objects.filter(user_type__code_description='Usuario')
    context = {
        'renters': renters,
        'book': book,
    }

    # Verificar se o usuário está autenticado e tem um perfil de usuário
    if request.user.is_authenticated and hasattr(request.user, 'user_type') and request.user.user_type is not None: 
        # Verificar se o usuário é um bibliotecário
        if request.user.user_type.user_code == 1:
            if request.method == 'POST':
                expected_return_date = request.POST.get('expected_return_date')
                status = request.POST.get('status')
                renter_id = request.POST.get('renter')
                loan_date = datetime.datetime.now()
                try:
                    renter = UserProfile.objects.get(pk=renter_id)
                except UserProfile.DoesNotExist:
                    messages.error(request, 'Usuário não encontrado.')
                    return redirect('emprestimos', book_id=book_id)
                Loans.objects.create(
                    book=book,
                    loaner=request.user,
                    renter=renter,
                    loan_date=loan_date,
                    expected_return_date=expected_return_date,
                    status=status,
                )
                # Para alterar o status do livro para 'Emprestado' temos que dar um get no status, só passar como status = 'Emprestado' não vai servir'
                book.status = Status.objects.get(name='Emprestado')
                book.save()
                messages.success(request, 'Empréstimo registrado com sucesso!')
                return redirect('detalhes-livro', book_id=book_id)
            else:
                return render(request, "biblioteca/emprestimos.html", context)
        else:
            return HttpResponse('Acesso negado: Você não é um bibliotecário.')
    else:
        return HttpResponse('Acesso negado: Você não está autenticado ou não tem um tipo de usuário associado.')


@login_required(login_url='/auth/entrar/') 
def devolucao(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    context = {
        'book': book,
    }
    if request.user.is_authenticated and hasattr(request.user, 'user_type') and request.user.user_type is not None: 
        if request.user.user_type.user_code == 1:
            if request.method == 'POST':
                try:
                    loan = Loans.objects.get(book = book,return_date__isnull=True )
                except Loans.DoesNotExist:
                    messages.error(request, 'Nenhum empréstimo ativo encontrado para este livro.')
                    return redirect('detalhes-livro', book_id=book_id)
                loan.return_date = datetime.datetime.now()
                loan.status = 'Devolvido' 
                loan.save()
                book_status_disponivel = Status.objects.get(name='Disponivel')
                book.status = book_status_disponivel
                book.save()
                messages.success(request, 'Devolução registrada com sucesso!')
                return redirect('detalhes-livro', book_id=book_id)
            else:
                return render(request, "biblioteca/detalhes-livro.html", context)
        else:
            return HttpResponse('Acesso negado: Você não é um bibliotecário.')
    else:
        return HttpResponse('Acesso negado: Você não está autenticado ou não tem um tipo de usuário associado.')
