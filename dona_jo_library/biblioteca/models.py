from django.db import models


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
    genre = models.CharField(max_length=40, blank=True)
    status = models.CharField(
        max_length=40, blank=True
    )  # status para dizer se está emprestado ou não, ou algum outro status
    rating = models.CharField(max_length=50, blank=True)
    item_type = models.CharField(
        max_length=50
    )  # atributo existente na planilha do André
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


# class Genres(models.Model):
#     name = models.CharField()


# Modelo para empréstimos
class Loans(models.Model):
    status = models.CharField(max_length=100)  # para status do empréstimo, ex: atrasado
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="loans")
    person_loan = models.ForeignKey(
        "Persons",
        on_delete=models.CASCADE,
        related_name="person_loans",
        # Person.TypeUser ==  1
    )
    responsible_librarian = models.ForeignKey(
        "Librarians",
        on_delete=models.CASCADE,
        related_name="loan_responsible_librarian",
        # Person.TypeUser ==  2
    )
    loan_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True, null=True)
    expected_return_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"


# Modelo de Pessoa
class Persons(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=11)
    birth_date = models.DateField()
    full_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    responsible_document = models.CharField(max_length=11, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"


# Modelo de Responsável (para quando Pessoa for menor de idade)
class Responsibles(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    birth_date = models.DateField()
    full_address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Responsible"
        verbose_name_plural = "Responsibles"


# Modelo de Bibliotecário
class Librarians(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    birth_date = models.DateField()
    full_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Librarian"
        verbose_name_plural = "Librarians"


# EmprestimoResponsavel, para vincular um responsável a um empréstimo
class LoanResponsibles(models.Model):
    loan = models.ForeignKey(
        Loans, on_delete=models.CASCADE, related_name="loan_responsibles"
    )
    responsible = models.ForeignKey(
        Responsibles, on_delete=models.CASCADE, related_name="loan_responsibles"
    )

    class Meta:
        verbose_name = "LoanResponsible"
        verbose_name_plural = "LoanResponsibles"


# EmprestimoBibliotecario, para vincular um bibliotecário a um empréstimo
class LoanLibrarians(models.Model):
    loan = models.ForeignKey(
        Loans, on_delete=models.CASCADE, related_name="loan_librarians"
    )
    librarian = models.ForeignKey(
        Librarians, on_delete=models.CASCADE, related_name="loan_librarians"
    )

    class Meta:
        verbose_name = "LoanLibrarian"
        verbose_name_plural = "LoanLibrarians"
