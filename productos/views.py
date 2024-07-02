from django.shortcuts import render
from .models import Producto, Categoria
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request, "home.html")

def mujer(request):
    categoria_mujer = get_object_or_404(Categoria, nombre="Mujer")
    productos = Producto.objects.filter(categoria=categoria_mujer)
    context = {"productos": productos}
    return render(request, 'mujer.html', context)

def hombre(request):
    categoria_hombre = get_object_or_404(Categoria, nombre="Hombre")
    productos = Producto.objects.filter(categoria=categoria_hombre)
    context = {"productos": productos}
    return render(request, 'hombre.html', context)

def ninno(request):
    categoria_ninno = get_object_or_404(Categoria, nombre="Niño")
    productos = Producto.objects.filter(categoria=categoria_ninno)
    context = {"productos": productos}
    return render(request, 'ninno.html', context)