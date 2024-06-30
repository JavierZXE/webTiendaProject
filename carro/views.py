from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Producto, Carrito

# Create your views here.
'''
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    carrito.agregar_producto(producto)
    return redirect('nombre_de_tu_vista_de_carrito')

def eliminar_del_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito.eliminar_producto(producto)
    return redirect('nombre_de_tu_vista_de_carrito')

def actualizar_cantidad_carrito(request, producto_id, cantidad):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = get_object_or_404(Carrito, usuario=request.user)
    carrito.actualizar_cantidad(producto, cantidad)
    return redirect('nombre_de_tu_vista_de_carrito')
'''