from django.urls import path
from App.views import *



urlpatterns = [
    path('home/', home, name="Home"),
    path('tienda/', tienda, name="Tienda"),
    
]

