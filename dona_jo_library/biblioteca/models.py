from django.db import models


class Livro(models.Model):
    nome = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100, blank=True)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=255, blank=True)
    ano = models.CharField(max_length=10)
    genero = models.CharField(max_length=40)
    status = models.IntegerField()
    classificacao_indicativa = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Emprestimo(models.Model):
    status = models.CharField(max_length=100)
    livro = models.ForeignKey(
        Livro, on_delete=models.CASCADE, related_name="emprestimos"
    )
    pessoa = models.ForeignKey(
        "Pessoa", on_delete=models.CASCADE, related_name="emprestimos_pessoa"
    )
    responsavel_emprestimo = models.ForeignKey(
        "Responsavel", on_delete=models.CASCADE, related_name="emprestimos_emprestavel"
    )
    bibliotecario_responsavel = models.ForeignKey(
        "Bibliotecario",
        on_delete=models.CASCADE,
        related_name="emprestimos_bibliotecario_responsavel",
    )
    data_emprestimo = models.DateTimeField()
    data_devolucao = models.DateTimeField(blank=True, null=True)
    data_devolucao_prevista = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    logradouro = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Responsavel(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    logradouro = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Bibliotecario(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20)
    idade = models.IntegerField()
    logradouro = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=20, blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmprestimoResponsavel(models.Model):
    emprestimo = models.ForeignKey(
        Emprestimo, on_delete=models.CASCADE, related_name="responsaveis_emprestimo"
    )
    responsavel = models.ForeignKey(
        Responsavel, on_delete=models.CASCADE, related_name="emprestimos_responsavel"
    )


class EmprestimoBibliotecario(models.Model):
    emprestimo = models.ForeignKey(
        Emprestimo, on_delete=models.CASCADE, related_name="bibliotecarios_emprestimo"
    )
    bibliotecario = models.ForeignKey(
        Bibliotecario,
        on_delete=models.CASCADE,
        related_name="emprestimos_bibliotecario",
    )
