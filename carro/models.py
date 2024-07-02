from django.db import models
from usuarios.models import Usuario
from productos.models import Producto

class Carrito(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, verbose_name='Usuario')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    actualizado = models.DateTimeField(auto_now=True, verbose_name='Última Actualización')

    def __str__(self):
        return f'Carrito de {self.usuario.nombre} {self.usuario.apellido}'

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items', verbose_name='Carrito')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.PositiveIntegerField(default=1, verbose_name='Cantidad')

    def __str__(self):
        return f'{self.cantidad} x {self.producto.descripcion} en el carrito de {self.carrito.usuario.nombre} {self.carrito.usuario.apellido}'

    class Meta:
        unique_together = ('carrito', 'producto')