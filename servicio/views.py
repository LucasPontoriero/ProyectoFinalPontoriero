from django.shortcuts import render

from servicio.models import servicios


def servicio(request):
    servicio1=servicios.objects.all()
    return render(request, "servicio/servicio.html", {"servicio1": servicio1})