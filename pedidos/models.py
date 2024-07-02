from django.db import models


class FormaPago(models.Model):
    nombre = models.CharField(unique=True,max_length=20)
    activo = models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Forma de Pago'
        verbose_name_plural = 'Formas de pago'
        ordering = ['nombre']
