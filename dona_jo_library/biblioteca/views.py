from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from biblioteca.models import Books, Loans, Genres, Status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def cadastrar(request):
    return render(request, "biblioteca/cadastrar.html")

def livros(request):
    books = Books.objects.filter(status__name='Disponivel')
    return render(request, "biblioteca/livros.html", {'books': books})

def detalhes_livro(request, book_id):
    book = get_object_or_404(Books, pk=book_id)
    
    # Verificar se o usuário está autenticado
    if request.user.is_authenticated:
        # Verificar se o usuário tem um perfil associado
        if hasattr(request.user, 'user_type') and request.user.user_type is not None:
            # Verificar se o usuário é um bibliotecário
            if request.user.user_type.code_description == 'Bibliotecario':
                return render(request, 'biblioteca/detalhes-livro.html', {'book': book})
    
    # Se o usuário não estiver autenticado ou não for um bibliotecário, redirecione ou retorne uma mensagem de erro
    return render(request, 'biblioteca/detalhes-livro.html', {'book': book})


# @login_required(login_url='/auth/entrar/') 
# def emprestimos(request):
#     # Verificar se o usuário está autenticado e tem um perfil de usuário
#     if request.user.is_authenticated and hasattr(request.user, 'user_type') and request.user.user_type is not None: 
#         # Verificar se o usuário é um bibliotecário
#         if request.user.user_type.user_code == 1:
#             return render(request, "biblioteca/emprestimos.html")
#         else:
#             return HttpResponse('Acesso negado: Você não é um bibliotecário.')
#     else:
#         # Se o usuário não estiver autenticado ou não tiver um tipo de usuário associado
#         return HttpResponse('Acesso negado: Você não está autenticado ou não tem um tipo de usuário associado.')



@login_required(login_url='/auth/entrar/') 
def emprestimos(request):
    renters = UserProfile.objects.filter(user_type__code_description='Usuario')
    context = {
        'renters': renters,
    }
    # Verificar se o usuário está autenticado e tem um perfil de usuário
    if request.user.is_authenticated and hasattr(request.user, 'user_type') and request.user.user_type is not None: 
        # Verificar se o usuário é um bibliotecário
        if request.user.user_type.user_code == 1:
            if request.method == 'POST':
                # Processar os dados do formulário de empréstimo
                # Aqui você pode acessar os dados do formulário usando request.POST
                # Por exemplo:
                book_id = request.POST.get('book_id')
                loan_date = request.POST.get('loan_date')
                # Processar outros campos do formulário conforme necessário

                # Verificar se o livro existe
                try:
                    book = Books.objects.get(pk=book_id)
                except Books.DoesNotExist:
                    messages.error(request, 'Livro não encontrado.')
                    return redirect('emprestimos')

                # Criar o empréstimo
                loan = Loans.objects.create(
                    book=book,
                    loaner=request.user,  # Usuário autenticado
                    loan_date=loan_date,
                    # Defina outros campos do empréstimo conforme necessário
                )

                # Redirecionar para a página de detalhes do livro
                return redirect('detalhes_livro', book_id=book_id)
            else:
                return render(request, "biblioteca/emprestimos.html", context)
        else:
            return HttpResponse('Acesso negado: Você não é um bibliotecário.')
    else:
        # Se o usuário não estiver autenticado ou não tiver um tipo de usuário associado
        return HttpResponse('Acesso negado: Você não está autenticado ou não tem um tipo de usuário associado.')


# class Loans(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     status = models.CharField(max_length=100)  # para status do empréstimo, ex: atrasado
#     book = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name="loans")
#     loaner = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name="loaner_loans",blank= True, null=True)
#     renter = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name="renter_loans",blank= True, null= True)
#     loan_date = models.DateTimeField()
#     return_date = models.DateTimeField(blank=True, null=True)
#     expected_return_date = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         verbose_name = "Loan"
#         verbose_name_plural = "Loans"