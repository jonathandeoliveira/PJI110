from django.contrib import admin

# Register your models here.
from users.models import UserTypes, Users

admin.site.register(UserTypes)
admin.site.register(Users)
