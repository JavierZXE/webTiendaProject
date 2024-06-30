from django.db import models
from carro.models import Carro
from usuarios.models import Usuario


class FormaPago(models.Model):
    nombre = models.CharField(max_length=20)
    activo = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de pago'
        ordering = ['nombre']

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    carrito = models.ForeignKey(Carro , on_delete=models.CASCADE, verbose_name='Carrito')
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Pedido')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total')
    pago = models.ForeignKey(FormaPago, on_delete=models.SET_NULL, null=True, verbose_name='Forma de Pago')

    def __str__(self):
        return f"Pedido #{self.id} de {self.usuario.nombre} - {self.pago.nombre}"
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha_pedido']
