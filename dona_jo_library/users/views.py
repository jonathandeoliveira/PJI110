from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
import traceback
from hashlib import sha256


#
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
#


def entrar(response):
    return render(response, "users/entrar.html")


def cadastrar(response):
    status = response.GET.get('status')
    return render(response, "users/cadastrar.html", {'status': status})


# def validate_user(request):
#     first_name = request.POST.get("first-name")
#     last_name = request.POST.get("last-name")
#     birth_date = request.POST.get("birthdate")
#     document = request.POST.get("document")
#     full_address = request.POST.get("address")
#     city = request.POST.get("city")
#     state = request.POST.get("state")
#     postal_code = request.POST.get("postal-code")
#     phone = request.POST.get("phone-number")
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     user_type = UserTypes.objects.get(user_code= 2)

#     user = UserProfile.objects.filter(email=email)

#     if not (first_name and email and document):
#         return redirect("/auth/cadastrar/?status=1")
#     if len(first_name.strip()) == 0 or len(email.strip()) == 0 or len(document.strip()) == 0: 
#          return redirect("/auth/cadastrar/?status=2")

#     if len(password) < 8:
#         return redirect("/auth/cadastrar/?status=3")

#     if len(user) > 0:
#         return redirect("/auth/cadastrar/?status=0")

#     try:
#         password = sha256(password.encode()).hexdigest()
#         login_user =  User.objects.create(username= email, email = email, password = password )
#         user_profile = UserProfile (
#             document=document,
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             birth_date=birth_date,
#             full_address=full_address,
#             city=city,
#             state=state,
#             postal_code=postal_code,
#             phone=phone,
#             user_type=user_type,
#             user = login_user
#         )
#         user_profile.save()

#         return redirect("/auth/cadastrar/?status=0")
#     except Exception as e:
#         traceback.print_exc()  # Imprime o traceback do erro
#         return  redirect("/auth/cadastrar/?status=4")



def validate_user(request):
    if request.method == "POST":
        # Obter os dados do formulário
        username =request.POST.get("username")
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        birth_date = request.POST.get("birthdate")
        document = request.POST.get("document")
        full_address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        postal_code = request.POST.get("postal-code")
        phone = request.POST.get("phone-number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_type = UserTypes.objects.get(user_code=2)

        # Verificar se todos os campos obrigatórios estão presentes
        if not all([first_name, email, document]):
            return redirect("/auth/cadastrar/?status=1")

        # Validar o comprimento dos campos
        if any(len(field.strip()) == 0 for field in [first_name, email, document]):
            return redirect("/auth/cadastrar/?status=2")

        # Validar a senha
        if len(password) < 8:
            return redirect("/auth/cadastrar/?status=3")

        # Verificar se o usuário já existe
        if UserProfile.objects.filter(email=email).exists():
            return redirect("/auth/cadastrar/?status=0")

        try:
            # Criar um novo usuário
            # user = User.objects.create_user(
            #    username=email, email=email, password=password
            #)
            #password = sha256(password.encode()).hexdigest()
    
            user_profile = UserProfile (
                username = username,
                document=document,
                email=email,
                first_name=first_name,
                last_name=last_name,
                birth_date=birth_date,
                full_address=full_address,
                city=city,
                state=state,
                postal_code=postal_code,
                phone=phone,
                password = password
            )
            user_profile.set_password(password)
            
            user_profile.save()
            
            return redirect("/auth/cadastrar/?status=0")
        except Exception as e:
            print(e)  # Tratar o erro apropriadamente
            return redirect("/auth/cadastrar/?status=4")

    else:
        return HttpResponse("Method not allowed", status=405)


def validates_login(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = UserProfile.objects.filter(email=email).first()  # Retrieve the first UserProfile object
    if user is None:
        return redirect("/auth/login/?status=1")  # User does not exist
    elif user.check_password(password):
        return HttpResponse(f'{email}{user.password}')  # Password is correct
    else:
        return redirect("/auth/login/?status=2")  # Password is incorrect
