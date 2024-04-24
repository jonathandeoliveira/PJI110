from django.contrib import admin

# Register your models here.
from users.models import UserTypes, Users


@admin.register(Users)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ("email", "password", "document")


admin.site.register(UserTypes)
