from django.contrib import admin
from .models import Usuario, TipoDeUsuario
# Register your models here.

admin.site.register(Usuario)
admin.site.register(TipoDeUsuario)