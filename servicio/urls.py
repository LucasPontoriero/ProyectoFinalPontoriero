from django.urls import path
from servicio.views import servicios



urlpatterns = [
    path('', servicios, name="Servicio"),
    
]

