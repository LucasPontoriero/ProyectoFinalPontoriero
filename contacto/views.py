from django.shortcuts import render, redirect
from .forms import Formulario

def contacto(request):
    formulario_contacto=Formulario()
    if request.method=="POST":
        formulario_contacto=Formulario(data= request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")
            return redirect('Contacto')
    return render(request, "contacto/contacto.html", {'miFormulario': formulario_contacto})