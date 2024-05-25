from django.urls import path
from biblioteca import views
from users.models import UserProfile, UserTypes

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path('biblioteca/emprestimos/<int:book_id>/', views.emprestimos, name='emprestimos'),
    path("cadastrar-livro/", views.cadastrar_livro, name="cadastrar_livro"),
    path("valida_cadastro_livro/", views.valida_cadastro_livro, name='valida_cadastro_livro'),
    path("livros/", views.livros, name="livros"),
    path('detalhes-livro/<int:book_id>/', views.detalhes_livro, name='detalhes-livro'),
    path('biblioteca/devolucao/<int:book_id>/', views.devolucao, name='devolucao'),
    path('livros/atualiza-livro/<int:book_id>/', views.atualiza_livro, name='atualiza-livro'),
    path('livros/atualiza-cadastro-livro/<int:book_id>/', views.atualiza_cadastro_livro, name='atualiza_cadastro_livro'),
]