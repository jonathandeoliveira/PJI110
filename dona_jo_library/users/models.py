from django.db import models
#
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
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

class UserProfile(AbstractUser):
    # Definindo os validadores personalizados
    postal_code_validator = RegexValidator( regex=r'^\d{8}$', message='O CEP deve ter 8 dígitos, exemplo: 12345678.')
    document_validator = RegexValidator( regex=r'^\d{11}$', message='O CPF deve ter 11 dígitos, exemplo: 19876543210.')
    phone_validator = RegexValidator( regex=r'^\d{11}$', message='Insira o telefone com o DDD, exemplo: 11912341234.')

    # Adicionando as regras de validação aos campos
    document = models.CharField(max_length=14, validators=[document_validator], unique=True)
    postal_code = models.CharField(max_length=12, validators = [postal_code_validator])
    phone = models.CharField(max_length=14, validators=[phone_validator])
    birth_date = models.DateField()
    
    def clean(self):
        super().clean()
        if self.birth_date > timezone.now().date():
            raise ValidationError({'birth_date': 'A data de nascimento não pode ser no futuro.'})
    
    full_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    user_type = models.ForeignKey(UserTypes, on_delete=models.DO_NOTHING, related_name="user_type", null=True)
    email = models.CharField(max_length=100, unique=True, blank=True)
    
    REQUIRED_FIELDS = ['document', 'birth_date', 'full_address', 'postal_code', 'phone']
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"

    def __str__(self):
        return self.username
