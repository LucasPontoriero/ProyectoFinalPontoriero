from django.db import models

class servicios(models.Model):
    titulo=models.CharField(max_length=40)
    contenido=models.CharField(max_length=300)
    imagen=models.ImageField(upload_to='servicio')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo
