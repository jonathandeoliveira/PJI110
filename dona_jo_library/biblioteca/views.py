from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Genres, Status
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile
from biblioteca.models import Books, Loans, Genres, Status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

def home(request):
    return render(request, "biblioteca/home.html")

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
def cadastrar_livro(request):
    return render(request, "biblioteca/cadastrar-livro.html")


def valida_cadastro_livro(request):
    if request.method == 'POST':
        # Recebendo os dados do formulário
        title = request.POST.get("title")
        ean_isbn13 = request.POST.get("ean_isbn13")
        upc_isbn10 = request.POST.get("upc_isbn10")
        author_first_name = request.POST.get("author_first_name")
        author_last_name = request.POST.get("author_last_name")
        publisher = request.POST.get("publisher")
        description = request.POST.get("description")
        year = request.POST.get("year")
        genre_name = request.POST.get("genre")
        status_name = request.POST.get("status")
        rating = request.POST.get("rating")  
        item_type = request.POST.get("item_type")  

        # Verificando se todos os campos obrigatórios estão presentes
        if not all([title, ean_isbn13, upc_isbn10, author_first_name, author_last_name, publisher, description, year, genre_name, status_name, item_type]):
            return HttpResponse("Todos os campos devem ser preenchidos.")

        # Verificando se o gênero e o status fornecidos existem no banco de dados // Precisa cadastrar os Gêneros e Status que vamos utilizar
        genre = Genres.objects.filter(name=genre_name).first()
        status = Status.objects.filter(name=status_name).first()
        
        if not genre or not status:
            # Se o gênero ou status não existem, retorne uma mensagem de erro
            return HttpResponse("O gênero ou status fornecido não existe.")

        # Criando um novo objeto Books e salvando-o no banco de dados
        new_book = Books.objects.create(
            title=title,
            ean_isbn13=ean_isbn13,
            upc_isbn10=upc_isbn10,
            author_first_name=author_first_name,
            author_last_name=author_last_name,
            publisher=publisher,
            description=description,
            year=year,
            genre=genre,
            status=status,
            rating=rating if rating else None,
            item_type=item_type
        )

        # Retornando uma mensagem de sucesso
        return HttpResponse("Livro cadastrado com sucesso.")
        
    else:
        # Se o método HTTP não for POST, retorne uma mensagem de erro
        return HttpResponse("O método HTTP esperado é POST.")
	
# Atualiza Cadastro de Livros 
def atualiza_livro(request):
    return render(request, "biblioteca/atualiza-livro.html")

def atualiza_cadastro_livro(request, livro_id):
    # Obtém o livro existente do banco de dados
    livro = get_object_or_404(Books, id=livro_id)

    if request.method == "POST":
        # Recebendo os dados do formulário
        dados_formulario = request.POST

        # Atualizando os dados do livro com base nos dados do formulário
        livro.title = dados_formulario.get("title", livro.title)
        livro.ean_isbn13 = dados_formulario.get("ean_isbn13", livro.ean_isbn13)
        livro.upc_isbn10 = dados_formulario.get("upc_isbn10", livro.upc_isbn10)
        livro.author_first_name = dados_formulario.get(
            "author_first_name", livro.author_first_name)
        livro.author_last_name = dados_formulario.get(
            "author_last_name", livro.author_last_name)
        livro.publisher = dados_formulario.get("publisher", livro.publisher)
        livro.description = dados_formulario.get(
            "description", livro.description)
        livro.year = dados_formulario.get("year", livro.year)

        # Verificando se o gênero e o status fornecidos existem no banco de dados
        genre_name = dados_formulario.get("genre")
        status_name = dados_formulario.get("status")
        genre = Genres.objects.filter(name=genre_name).first()
        status = Status.objects.filter(name=status_name).first()

        if not genre or not status:
            # Se o gênero ou status não existem, retorne uma mensagem de erro
            return HttpResponse("O gênero ou status fornecido não existe.")

        livro.genre = genre
        livro.status = status

        livro.rating = dados_formulario.get("rating", livro.rating)
        livro.item_type = dados_formulario.get("item_type", livro.item_type)

        # Salvando as alterações no banco de dados
        livro.save()

        # Retornando uma mensagem de sucesso
        return HttpResponse("Livro atualizado com sucesso.")

    else:
        # Se o método HTTP não for POST, retorne uma mensagem de erro
        return HttpResponse("O método HTTP esperado é POST.")
