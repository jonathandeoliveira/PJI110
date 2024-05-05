from django.shortcuts import render
from django.http import HttpResponse
from .models import Books, Genres, Status

def home(request):
    return render(request, "biblioteca/home.html")


def cadastrar(request):
    return render(request, "biblioteca/cadastrar.html")


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

