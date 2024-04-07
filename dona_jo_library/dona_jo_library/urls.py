from django.contrib import admin
from django.urls import path

from biblioteca.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
]
