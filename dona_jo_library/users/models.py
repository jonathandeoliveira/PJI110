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