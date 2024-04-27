from django.db import models


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
class Users(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    birth_date = models.DateField()
    full_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=64)
    user_type = models.ForeignKey(
        UserTypes, on_delete=models.DO_NOTHING, related_name="user_types"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name
