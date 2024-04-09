from django.urls import path

# importa arquivo views.py da pasta atual (no nosos caso, biblioteca)
from . import views

# também poderia ser como abaixo:
# from biblioteca import views


urlpatterns = [
    path("cadastrar/", views.cadastrar),
]
