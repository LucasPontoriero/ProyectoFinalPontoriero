from django.shortcuts import render

from servicio.models import servicio


def servicios(request):
    servicio1=servicio.objects.all()
    return render(request, "servicio/servicio.html", {"servicio1": servicio1})