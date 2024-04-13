from django.db import models


# Create your models here.

# Modelo de Usuário
# class Users(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     document = models.CharField(max_length=20)
#     birth_date = models.DateField()
#     full_address = models.CharField(max_length=255)
#     city = models.CharField(max_length=100, blank=True)
#     state = models.CharField(max_length=100, blank=True)
#     postal_code = models.CharField(max_length=20)
#     phone = models.CharField(max_length=20)
#     email = models.CharField(max_length=100, blank=True)
#     ###
#     user_type = models.ForeignKey(
#       #IF site.com/usarios/cadastro
#        # cadastrar como usuario ou responsavel
#       #ELSE caminho = site.com/ADM/USUARIOS/CADASTRO
#       # cadastrar como usuario, bibliotecario ou responsável
#                                 )
#     ###

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class TypeUser(models.Model):
#       type_user = models.IntegerField()
#       type_name = models.CharField()
#       ###
#       type_user = 1
#       type_name = "usuário"
#       ##
#         type_user = 2
#         type_name = "Bibliotecário"
#       ##
#       type_user = 3
#       type_name = "Responsável"
#       ##
#       type_user = 4
#       type_name = "Administrador"
#       ##
