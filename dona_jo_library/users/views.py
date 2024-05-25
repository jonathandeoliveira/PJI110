from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import UserProfile, UserTypes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import pdb

def entrar(response):
    return render(response, "users/entrar.html")



def cadastrar(response):
    user_types = UserTypes.objects.all()
    status = response.GET.get('status')
    return render(response, "users/cadastrar.html", {'status': status, 'user_types': user_types})


#antes de iniciar a alteração do cadastro, o sistema deverá perguntar o CPF ou o Username.
def alterar_cadastro(response):
    status = response.GET.get('status')
    return render(response, "users/alterar_cadastro.html", {'status': status})


def validate_user(request):
    if request.method == "POST":
        # pdb.set_trace()
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
        user_type = request.POST.get("user-type")                   # DISCUTIR REGRA DE CADASTRO COM O REPRESENTANTE DA ONG
        user_type = UserTypes.objects.get(code_description = user_type)
        #if not all([first_name, email, document]):
            #return redirect("/auth/cadastrar/?status=1")
        #if any(len(field.strip()) == 0 for field in [first_name, email, document]):
            #return redirect("/auth/cadastrar/?status=2")
        #if len(password) < 8:
            #return redirect("/auth/cadastrar/?status=3")
        #if UserProfile.objects.filter(email=email).exists():
            #return redirect("/auth/cadastrar/?status=0")
        try:
            #pdb.set_trace()
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
                password = password,
                user_type = user_type
            )
            user_profile.set_password(password)

            user_profile.save()
            
            return redirect("/auth/cadastrar/?status=0")
        except Exception as e:
            return redirect("/auth/cadastrar/?status=4")

    else:
        return HttpResponse("Method not allowed", status=405)

    

    
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
        # Verificar se todos os campos obrigatórios estão presentes
        # if not all([first_name, email, document]):
        #     return redirect("/auth/alterar_cadastro/?status=1")

        # Validar o comprimento dos campos
        # if any(len(field.strip()) == 0 for field in [first_name, email, document]):
        #     return redirect("/auth/alterar_cadastro/?status=2")

        # Validar a senha
        # if len(password) < 8:
        #     return redirect("/auth/alterar_cadastro/?status=3")

        # Verificar se o usuário já existe
        # if UserProfile.objects.filter(email=email).exists():
        #     return redirect("/auth/alterar_cadastro/?status=0")

        try:
            user_profile_update = UserProfile.objects.get(username=username, document=document)
            if user_profile_update != None: 
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
        
        
        
        
def validates_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, 'Usuário ou senha inválidos. Tente novamente.')
            return redirect('/auth/entrar/')
        else:
            login(request, user)
            messages.success(request, f'{username} logado com sucesso')
            return redirect('/')
    return redirect('/auth/entrar/')
    
@login_required(login_url='/auth/entrar/')
def sair(request):
    logout(request)
    messages.success(request, 'Deslogado com sucesso!')
    return redirect('/')


@login_required(login_url='/auth/entrar/')
def myaccount(request):
    user = request.user
    user_type = user.user_type
    if user_type:
        user_type_description = user_type.code_description
        return HttpResponse(f'Está autenticado como: {user.username}. Tipo de usuário: {user_type_description}')
    else:
        messages.error(request, 'Você não tem permissão para acessar esta página.')
        return redirect('/auth/entrar/')

