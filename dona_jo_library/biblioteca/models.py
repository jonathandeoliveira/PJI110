from django.db import models
from users.models import Users, UserTypes


# Tabela para os gêneros/categorias de livros
class Genres(models.Model):
    name = models.CharField()
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


# status para dizer se está emprestado ou não, ou algum outro status específico: perdido, danificado, etc.
class Status(models.Model):
    name = models.CharField()
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


# Modelo para Livros
class Books(models.Model):
    title = models.CharField(max_length=100)
    ean_isbn13 = models.CharField(max_length=13, blank=True)
    upc_isbn10 = models.CharField(max_length=10, blank=True)
    author_first_name = models.CharField(max_length=100, blank=True)
    author_last_name = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=10, blank=True)
    genre = models.ForeignKey(Genres, on_delete=models.DO_NOTHING, related_name="genre")
    status = models.ForeignKey(
        Status, on_delete=models.DO_NOTHING, related_name="status"
    )
    rating = models.CharField(max_length=50, blank=True)
    # atributo existente na planilha do André
    item_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Status(models.Model):
    name = models.CharField()
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


# Modelo para empréstimos
class Loans(models.Model):
    status = models.CharField(max_length=100)  # para status do empréstimo, ex: atrasado
    book = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name="loans")
    loan_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    expected_return_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"


# Removendo para usar no app users
# # Modelo de Pessoa
# class Persons(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     document = models.CharField(max_length=11)
#     birth_date = models.DateField()
#     full_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100, blank=True)
#     state = models.CharField(max_length=100, blank=True)
#     postal_code = models.CharField(max_length=20)
#     phone = models.CharField(max_length=20)
#     email = models.CharField(max_length=100, blank=True)
#     responsible_document = models.CharField(max_length=11, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Person"
#         verbose_name_plural = "Persons"


# # Modelo de Bibliotecário
# class Librarians(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     document = models.CharField(max_length=20)
#     birth_date = models.DateField()
#     full_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100, blank=True)
#     state = models.CharField(max_length=100, blank=True)
#     postal_code = models.CharField(max_length=20)
#     phone = models.CharField(max_length=20)
#     email = models.CharField(max_length=100, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Librarian"
#         verbose_name_plural = "Librarians"
