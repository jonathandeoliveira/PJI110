from django.db import models
#

from django.contrib.auth.models import AbstractUser
#
class UserTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_code = models.IntegerField()
    code_description = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

 
    
    class Meta:
        verbose_name = "UserType"
        verbose_name_plural = "UserTypes"


# Modelo de Usuário
# class UserProfile(AbstractUser):
#     #
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
#     #
#     id = models.BigAutoField(primary_key=True)
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
#     password = models.CharField(max_length=64)
#     user_type = models.ForeignKey(
#         UserTypes, on_delete=models.DO_NOTHING, related_name="user_types"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#      # Campos obrigatórios para a criação de um usuário
#     REQUIRED_FIELDS = ['document', 'birth_date', 'full_address', 'postal_code', 'phone', 'user_type', 'email']

#     # Especifica que o campo de e-mail será usado como nome de usuário
#     USERNAME_FIELD = 'email'
    
#     class Meta:
#         verbose_name = "UserProfile"
#         verbose_name_plural = "User"
# #
#     def __str__(self):
#         return self.user.username
# #

class UserProfile(AbstractUser):
    document = models.CharField(max_length=20)
    birth_date = models.DateField()
    full_address = models.CharField(max_length=260)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    user_type = models.ForeignKey(UserTypes, on_delete=models.DO_NOTHING, related_name="user_type", null=True)
    email = models.CharField(max_length=100, unique=True, blank=True)
    
    REQUIRED_FIELDS = ['document', 'birth_date', 'full_address', 'postal_code', 'phone','email']

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"

    def __str__(self):
        return self.username