from django.shortcuts import render

def home(request):
    return render(request, "biblioteca/home.html")


def cadastrar(request):
    return render(request, "biblioteca/cadastrar.html")


def cadastrar_livro(request):
    return render(request, "biblioteca/cadastrar-livro.html")

def validate_books(request):
    title = request.POST.get("title")
    ean_isbn13 = request.POST.get("ean_isbn13")
    upc_isbn10 = request.POST.get("upc_isbn10")
    author_first_name = request.POST.get("author_first_name")
    author_last_name = request.POST.get("author_last_name")
    publisher = request.POST.get("publisher")
    description = request.POST.get("description")
    year = request.POST.get("year")
    genre = request.POST.get("genre")
    status = request.POST.get("status")
    rating = request.POST.get("rating")
    item_type = request.POST.get("item_type")

    book = Books.objects.filter(ean_isbn13 = ean_isbn13)

    if len(title.strip()) > 100 or title.strip() == 0:
         return redirect("/biblioteca/cadastrar-livro/?status=2")
    #nessa parte e nas de baixo gostaria de redirecionar pra um erro algo assim, só mantive o status=2 igual tava na validação do user
    if ean_isbn13.strip() == 0 and upc_isbn10.strip() == 0:
        return redirect("/biblioteca/cadastrar-livro/?status=2")
    if ean_isbn13.strip() > 13:
        return redirect("/biblioteca/cadastrar-livro/?status=2")
    if upc_isbn10.strip() > 10:
        return redirect("/biblioteca/cadastrar-livro/?status=2")
    if author_first_name.strip() > 100 or author_first_name.strip() == 0:
        return redirect("/biblioteca/cadastrar-livro/?status=2")
    if author_last_name.strip() > 100 or author_last_name.strip() == 0:
        return redirect("/biblioteca/cadastrar-livro/?status=2")
    if publisher.strip() > 255 or publisher.strip() == 0:
        return redirect("/biblioteca/cadastrar-livro/?status=2")
    if year.strip() == 0:
        return redirect("/biblioteca/cadastrar-livro/?status=2")
    if status.strip() == 0:
        return redirect("/biblioteca/cadastrar-livro/?status=2")


    try:
        book = Books(
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
            rating=rating,
            item_type=item_type #fiquei na duvida tbm se o item_type é analogo ao user_types ou é um campo que vai pegar no html
        )
        book.save()
        return redirect("/biblioteca/cadastrar-livro/?status=1")
        #aqui tambem eu nao sei pra qual link redirecionar quando da certo
    except Exception as e:
        traceback.print_exc()  # Imprime o traceback do erro
        return  HttpResponse(f'{title}{ean_isbn13}{upc_isbn10}{author_first_name}{author_last_name}{publisher}{year}{status}')
