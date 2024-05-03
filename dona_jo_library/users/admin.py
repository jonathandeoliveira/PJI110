from django.contrib import admin

# Register your models here.
from users.models import UserTypes, UserProfile


@admin.register(UserProfile)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ("email", "password", "document")


admin.site.register(UserTypes)
