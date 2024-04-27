from django.contrib import admin
from django.urls import path, include
from biblioteca import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("biblioteca/", include("biblioteca.urls")),
    path("auth/", include("users.urls")),

]
