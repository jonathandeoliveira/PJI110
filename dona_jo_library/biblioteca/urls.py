from django.urls import path
from biblioteca import views
from users.models import UserProfile, UserTypes

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    #path("home/", views.home, name="home"),
    path('biblioteca/emprestimos/<int:book_id>/', views.emprestimos, name='emprestimos'),
    path("livros/", views.livros, name="livros"),
    path('detalhes-livro/<int:book_id>/', views.detalhes_livro, name='detalhes-livro'),
]
