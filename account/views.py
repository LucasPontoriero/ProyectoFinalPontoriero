from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from account.forms import UserRegisterForm
from account.models import Avatar

def login_account(request):
    if request.method == 'POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            user=authenticate(username=informacion['username'], password=informacion['password'])
            if user:
                login(request, user)
                return redirect("Home")
            else:
                return redirect ("Tienda")
            
    form = AuthenticationForm
    context= {
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request,"account/forms.html", context=context)

def register_account(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accountLogin")
    else:
        form = UserCreationForm()
    context = {
        "form": form,
        "titulo":"Registrar usuario",
        "enviar":"Registrar"
    }
    return render(request, "account/forms.html", context=context)

def editar_usuario(request):

    user=request.user
    if request.method=="POST":
        form=UserRegisterForm(request.POST, request.FILES)
        
        if form.is_valid():
            informacion=form.cleaned_data
            user.username=informacion["username"]
            user.email=informacion["email"]
            user.is_staff=informacion["is_staff"]

            try:
                user.avatar.imagen=informacion["imagen"]
            except:
                avatar=Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()
            

            user.save()
            return redirect("accountLogin")
        
        
    form=UserRegisterForm(initial={
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff
    })
    context={
        "form":form,
        "titulo":"Editar usuario",
        "enviar":"Editar"
    }
    return render(request, "account/forms.html", context=context)
