from django.urls import path
from .views import *



urlpatterns = [
    path('contacto/', contacto, name="Contacto"),
    path('<int:post_id>/', post_detail, name="post_detail")
]

