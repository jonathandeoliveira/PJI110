from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Genres, Status
from django.shortcuts import get_object_or_404

from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from biblioteca.models import Books, Loans, Genres, Status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "biblioteca/home.html")

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
