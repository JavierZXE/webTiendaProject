# Generated by Django 5.0.6 on 2024-06-24 00:58

import usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(help_text='Ingrese el RUT en el formato 12.345.678-9', max_length=15, primary_key=True, serialize=False, validators=[usuarios.models.validate_rut], verbose_name='RUT')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=100, verbose_name='Correo Electrónico')),
                ('region', models.CharField(max_length=100, verbose_name='Región')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('educacion', models.CharField(choices=[('Sin educación', 'Sin educación'), ('Educación Preescolar', 'Educación Preescolar'), ('Educación Básica', 'Educación Básica'), ('Educación Media', 'Educación Media'), ('Educación Superior', 'Educación Superior')], max_length=20, verbose_name='Nivel de Educación')),
                ('contraseña', models.CharField(max_length=128, verbose_name='Contraseña')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['apellido', 'nombre'],
            },
        ),
    ]
