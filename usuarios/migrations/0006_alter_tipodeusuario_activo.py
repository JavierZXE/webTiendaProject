# Generated by Django 5.0.6 on 2024-06-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_usuario_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipodeusuario',
            name='activo',
            field=models.BooleanField(default=False),
        ),
    ]
