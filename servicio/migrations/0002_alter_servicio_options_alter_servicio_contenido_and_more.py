# Generated by Django 4.1.7 on 2023-04-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
        migrations.AlterField(
            model_name='servicio',
            name='contenido',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='servicio'),
        ),
    ]