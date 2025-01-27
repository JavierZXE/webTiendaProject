# Generated by Django 5.0.6 on 2024-06-29 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carro', '0001_initial'),
        ('usuarios', '0002_tipodeusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('activo', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Forma de Pago',
                'verbose_name_plural': 'Formas de pago',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pedido')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carro.carro', verbose_name='Carrito')),
                ('pago', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pedidos.formapago', verbose_name='Forma de Pago')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['-fecha_pedido'],
            },
        ),
    ]
