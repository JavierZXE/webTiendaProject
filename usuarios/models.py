from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

def validate_rut(value):
    import re
    if not re.match(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$', value):
        raise ValidationError('Formato de RUT no válido')

    rut, dv = value.split('-')
    rut = rut.replace('.', '')

    suma = 0
    multiplo = 2

    for i in reversed(rut):
        suma += int(i) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2

    dv_calculado = 11 - (suma % 11)
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)

    if dv_calculado.upper() != dv.upper():
        raise ValidationError('Dígito verificador del RUT no válido')

class TipoDeUsuario(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Tipo de Usuario')
    activo = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre
    
def get_default_tipo_usuario():
    return None
    
class Usuario(models.Model):
    rut = models.CharField(
        primary_key=True,
        max_length=15,
        validators=[validate_rut],
        verbose_name='RUT',
        help_text='Ingrese el RUT en el formato 12.345.678-9'
    )
    nombre = models.CharField(max_length=50, verbose_name='Nombre')
    apellido = models.CharField(max_length=50, verbose_name='Apellido')
    correo = models.EmailField(max_length=100, verbose_name='Correo Electrónico')
    region = models.CharField(max_length=100, verbose_name='Región')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    tipo_usuario = models.ForeignKey(TipoDeUsuario, default=None, null=True, blank=True, on_delete=models.CASCADE , verbose_name='Tipo de usuario')
    EDUCACION_CHOICES = [
        ('Sin educación', 'Sin educación'),
        ('Educación Preescolar', 'Educación Preescolar'),
        ('Educación Básica', 'Educación Básica'),
        ('Educación Media', 'Educación Media'),
        ('Educación Superior', 'Educación Superior'),
    ]
    educacion = models.CharField(
        max_length=20,
        choices=EDUCACION_CHOICES,
        verbose_name='Nivel de Educación'
    )
    contraseña = models.CharField(max_length=128, verbose_name='Contraseña')

    def save(self, *args, **kwargs):
        self.contraseña = make_password(self.contraseña)
        super(Usuario, self).save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.rut})'

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['apellido', 'nombre']
