from django.urls import path
from biblioteca import views

urlpatterns = [
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("home/", views.home, name="home"),
]
