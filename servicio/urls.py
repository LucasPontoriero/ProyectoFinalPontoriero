from django.urls import path
from servicio.views import servicio


urlpatterns = [
    path('', servicio, name="Servicio"),
    
]

