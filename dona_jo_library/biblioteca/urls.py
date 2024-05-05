from django.urls import path
from biblioteca import views


urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("home/", views.home, name="home"),
    path("cadastrar-livro/", views.cadastrar_livro, name="cadastrar_livro"),
    path("valida_cadastro_livro/", views.valida_cadastro_livro, name='valida_cadastro_livro'),

]
