from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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


#antes de iniciar a alteração do cadastro, o sistema deverá perguntar o CPF ou o Username.
def alterar_cadastro(response):
    status = response.GET.get('status')
    return render(response, "users/alterar_cadastro.html", {'status': status})


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
        #user_type = UserTypes.objects.get(user_code=2)

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

 #FORMA 1 DE VALIDAR + AUTENTICAR 
# def validates_login(request):
#     email = request.POST.get("email")
#     password = request.POST.get("password")
#     #user = UserProfile.objects.filter(email=email).first()  # Retrieve the first UserProfile object
#     user_teste = authenticate(email = email, password = password)
#     if user_teste is None:
#         return redirect("/auth/login/?status=1")  
#     elif user_teste.check_password(password):
#         return HttpResponse(f'{email}{user_teste.password}') 
#     else:
#         return redirect("/auth/login/?status=2") 


# SEGUNDA FORMA DE VALIDAR
def validates_login(request):
    email = request.POST.get("email")
    username = request.POST.get("username")
    password = request.POST.get("password")
    # Authenticate the user
    user = authenticate(request, username= username, email= email, password=password)
    if user is None:
        # Autenticação falhou
        HttpResponse(f'Algo deu errado, tente novamente') 
    else:
        login(request, user)  # Usuario conseguiu logar
        print("Usuario logado")
        return redirect("{% url 'home'%}")
    
        # User authentication succeeded
        # Here, you don't need to check the password again because authenticate already did it
        #login(request, user)  # Log in the user
        #return HttpResponse(f'{email} logged in successfully') 
    
def update_user(request):
    
    #aqui a aplicação busca o usuário que será alterado no banco de dados.
    #user_profile_update= UserProfile(username) #pensar em buscar pelo CPF!!!
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
        # user_type = UserTypes.objects.get(user_code=0)

        # Verificar se todos os campos obrigatórios estão presentes
        if not all([first_name, email, document]):
            return redirect("/auth/cadastrar/?status=1")

        # Validar o comprimento dos campos
        if any(len(field.strip()) == 0 for field in [first_name, email, document]):
            return redirect("/auth/cadastrar/?status=2")

        # Validar a senha
        # if len(password) < 8:
        #     return redirect("/auth/cadastrar/?status=3")

        # Verificar se o usuário já existe
        # if UserProfile.objects.filter(email=email).exists():
        #     return redirect("/auth/cadastrar/?status=0")

        try:
            # Criar um novo usuário
            # user = User.objects.create_user(
            #    username=email, email=email, password=password
            #)
            #password = sha256(password.encode()).hexdigest()
            #user_profile_update = UserProfile.objects.filter(username=username, document=document)
            user_profile_update = UserProfile.objects.get(username=username, document=document)
            if user_profile_update != None: 
                # user_profile_update = UserProfile (
                #     # username = username,
                #     email=email,
                #     first_name=first_name,
                #     last_name=last_name,
                #     birth_date=birth_date,
                #     full_address=full_address,
                #     city=city,
                #     state=state,
                #     postal_code=postal_code,
                #     phone=phone,
                #     )
                user_profile_update.email=email
                user_profile_update.first_name=first_name
                user_profile_update.last_name=last_name
                user_profile_update.birth_date=birth_date
                user_profile_update.full_address=full_address
                user_profile_update.city=city
                user_profile_update.state=state
                user_profile_update.postal_code=postal_code
                user_profile_update.phone=phone
            # user_profile.set_password(password)
            
            # salva as alterações no local do user_profile
            user_profile_update.save()
            print(user_profile_update)
            return HttpResponse (user_profile_update)
            # return redirect("/auth/cadastrar/?status=0")
        except Exception as e:
            print(e)  # Tratar o erro apropriadamente
            return redirect("/auth/cadastrar/?status=4")

    else:
        return HttpResponse("Method not allowed", status=405)
        
@login_required(login_url='/auth/entrar/')    
def myaccount(request):
    user = request.user
    user_type = user.user_type.code_description
    return HttpResponse(f'Está autenticado como: {user.username}. Tipo de usuário: {user_type}')