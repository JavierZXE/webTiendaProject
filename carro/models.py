from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
# Create your models here.

class Carro(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name='Fecha de Creación')
    completado = models.BooleanField(default=False, verbose_name='Completado')

    def __str__(self):
        return f"Carrito de {self.usuario.nombre} - {'Completado' if self.completado else 'Activo'}"
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def agregar_producto(self, producto, cantidad=1):
        from productos.models import CarroProducto

        carro_producto, created = CarroProducto.objects.get_or_create(
            carrito=self,
            producto=producto,
            defaults={'cantidad': cantidad, 'precio_unitario': producto.precio}
        )
        if not created:
            carro_producto.cantidad += cantidad
            carro_producto.save()

    def eliminar_producto(self, producto):
        from productos.models import CarroProducto 
        
        try:
            carro_producto = CarroProducto.objects.get(carrito=self, producto=producto)
            carro_producto.delete()
        except CarroProducto.DoesNotExist:
            pass

    def actualizar_cantidad(self, producto, cantidad):
        from productos.models import CarroProducto
        
        try:
            carro_producto = CarroProducto.objects.get(carrito=self, producto=producto)
            carro_producto.cantidad = cantidad
            carro_producto.save()
        except CarroProducto.DoesNotExist:
            pass