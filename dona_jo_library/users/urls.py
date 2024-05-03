from django.urls import path
from users import views


urlpatterns = [
    path("entrar/", views.entrar, name="entrar"),
    path("cadastrar/", views.cadastrar, name="cadastrar"),
    path("validate_user/", views.validate_user, name="validate_user"),
    path("validates_login/", views.validates_login, name="validates_login"),
    path("alterar_cadastro/", views.update_user, name="update_user")
]
