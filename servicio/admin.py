from django.contrib import admin
from .models import servicios

class servicio_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(servicios, servicio_admin)


