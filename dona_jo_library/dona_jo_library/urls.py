from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("biblioteca/", include("biblioteca.urls", namespace='biblioteca')),
    #path("biblioteca/cadastrar-livro/", include("biblioteca.urls")),
    path("auth/", include("users.urls")),
    #path("auth/cadastrar/", include("users.urls")),
    path("", views.home, name ='home')


]
