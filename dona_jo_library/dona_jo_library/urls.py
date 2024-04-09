from django.contrib import admin
from django.urls import path, include

from biblioteca.views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("biblioteca/", include("biblioteca.urls")),
]
