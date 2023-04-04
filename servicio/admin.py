from django.contrib import admin
from .models import servicio

class servicio_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(servicio, servicio_admin)


