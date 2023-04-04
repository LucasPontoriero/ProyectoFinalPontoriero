from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "App/home.html")

def tienda(request):
    return render(request, "App/tienda.html")

