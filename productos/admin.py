from django.contrib import admin
from .models import Categoria, Producto, CarroProducto, Marca
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(CarroProducto)
admin.site.register(Marca)
