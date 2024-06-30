# Generated by Django 5.0.6 on 2024-06-29 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0001_initial'),
        ('productos', '0002_marca_producto_barcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarroProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1, verbose_name='Cantidad')),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Unitario')),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='carro.carro', verbose_name='Carro')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Producto en Carro',
                'verbose_name_plural': 'Productos en Carro',
                'unique_together': {('carro', 'producto')},
            },
        ),
    ]