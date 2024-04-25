from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from users.models import Users, UserTypes
import traceback

def entrar(response):
    return render(response, "users/entrar.html")


def cadastrar(response):
    return render(response, "users/cadastrar.html")


def validate_user(request):
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
    user_type = UserTypes.objects.get(user_code= 2)

    user = Users.objects.filter(email=email)

    if not (first_name and email and document):
        return redirect("/auth/cadastrar/?status=1")
    if len(first_name.strip()) == 0 or len(email.strip()) == 0 or len(document.strip()) == 0: 
         return redirect("/auth/cadastrar/?status=2")

    if len(password) < 8:
        return redirect("/auth/cadastrar/?status=3")

    if len(user) > 0:
        return redirect("/auth/cadastrar/?status=0")

    try:
        user = Users(
            document=document,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            full_address=full_address,
            city=city,
            state=state,
            postal_code=postal_code,
            phone=phone,
            user_type=user_type  # Passa o objeto UserTypes aqui
        )
        user.save()
        return redirect("/auth/cadastrar/?status=0")
    except Exception as e:
        traceback.print_exc()  # Imprime o traceback do erro
        return  HttpResponse(f'{first_name}{last_name}{birth_date}{full_address}{city}{state}{postal_code}{document}\n{email}\n{password}\n{phone}\n{user_type}')

