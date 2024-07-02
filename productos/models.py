from django.db import models
import shortuuid

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    activo = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

class Marca(models.Model):
    nombre = models.CharField(unique=True, max_length=100)
    activo = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['nombre']

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True, verbose_name='Imagen')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca")
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock')
    barcode = models.CharField(unique=True, max_length=13, blank=True, null=True, verbose_name='Codigo de Barras(No ingresar, ¡se genera solo!)')
    
    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = self.generate_unique_barcode()
        super().save(*args, **kwargs)

    def generate_unique_barcode(self):
        while True:
            barcode = shortuuid.ShortUUID(alphabet="0123456789").random(length=13)
            if not Producto.objects.filter(barcode=barcode).exists():
                return barcode

    def __str__(self):
        return f"{self.marca} - {self.descripcion} - Precio: {self.precio} - Stock: {self.stock}"
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['categoria', 'marca', 'descripcion']
