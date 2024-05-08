from django.urls import path
from biblioteca import views
from users.models import UserProfile, UserTypes

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("home/", views.home, name="home"),
    path("cadastrar-livro/", views.cadastrar_livro, name="cadastrar_livro"),
    path("valida_cadastro_livro/", views.valida_cadastro_livro, name='valida_cadastro_livro'),

    #path("home/", views.home, name="home"),
    path("emprestimos/", views.emprestimos, name="emprestimos"),
    path("livros/", views.livros, name="livros"),
]
