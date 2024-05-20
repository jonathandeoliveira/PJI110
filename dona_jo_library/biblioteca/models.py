from django.db import models
from django.conf import settings
from users.models import UserProfile, UserTypes
#
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#

# Tabela para os gêneros/categorias de livros

class Genres(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField() 
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

# status para dizer se está emprestado ou não, ou algum outro status específico: perdido, danificado, etc.
class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


# Modelo para Livros
class Books(models.Model):
    id = models.BigAutoField(primary_key=True) 
    title = models.CharField(max_length=100)
    ean_isbn13 = models.CharField(max_length=13, blank=True)
    upc_isbn10 = models.CharField(max_length=10, blank=True)
    author_first_name = models.CharField(max_length=100, blank=True)
    author_last_name = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=700, blank=True)
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

    def __str__(self) -> str:
        return self.title


# Modelo para empréstimos
class Loans(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=100)  # para status do empréstimo, ex: atrasado
<<<<<<< Updated upstream
    book = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name="loans")
    loaner = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name="loaner_loans",blank= True, null=True)
    renter = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name="renter_loans",blank= True, null= True)
=======
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="loans")
    person_loan = models.ForeignKey(
        "Persons",
        on_delete=models.CASCADE,
        related_name="person_loans",
    )
    responsible_librarian = models.ForeignKey(
        "Librarians",
        on_delete=models.CASCADE,
        related_name="loan_responsible_librarian",
    )
>>>>>>> Stashed changes
    loan_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    expected_return_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
