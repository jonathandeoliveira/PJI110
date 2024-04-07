from django.db import models


# Modelo para Livros
class Book(models.Model):
    title = models.CharField(max_length=100)
    ean_isbn13 = models.CharField(max_length=13, blank=True)
    upc_isbn10 = models.CharField(max_length=10, blank=True)
    author_first_name = models.CharField(max_length=100, blank=True)
    author_last_name = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=10, blank=True)
    genre = models.CharField(max_length=40, blank=True)
    status = models.IntegerField(blank=True)
    rating = models.CharField(max_length=50, blank=True)
    item_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Modelo para empréstimos
class Loan(models.Model):
    status = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    person = models.ForeignKey(
        "Person", on_delete=models.CASCADE, related_name="person_loans"
    )
    responsible_loan_manager = models.ForeignKey(
        "Librarian", on_delete=models.CASCADE, related_name="loan_manager_loans"
    )
    responsible_librarian = models.ForeignKey(
        "Librarian",
        on_delete=models.CASCADE,
        related_name="librarian_loans",
    )
    loan_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    expected_return_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Modelo de Pessoa
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=11)
    birth_date = models.DateField()
    full_adress = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Modelo de Responsável (para quando Pessoa for menor de idade)
class Responsible(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    birth_date = models.DateField()
    full_adress = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Modelo de Bibliotecário
class Librarian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    birth_date = models.DateField()
    full_adress = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# EmprestimoResponsavel, para vincular um responsável a um empréstimo
class LoanResponsible(models.Model):
    loan = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name="loan_responsibles"
    )
    responsible = models.ForeignKey(
        Responsible, on_delete=models.CASCADE, related_name="loan_responsibles"
    )


# EmprestimoBibliotecario, para vincular um bibliotecário a um empréstimo
class LoanLibrarian(models.Model):
    loan = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name="loan_librarians"
    )
    librarian = models.ForeignKey(
        Librarian,
        on_delete=models.CASCADE,
        related_name="loan_librarians",
    )
