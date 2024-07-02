from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from .models import Carrito, CarritoItem, Producto

# Create your views here.
@login_required(login_url='usuarios:login')
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    usuario_actual = request.user
    carrito, creado = Carrito.objects.get_or_create(usuario=usuario_actual)
    
    try:
        item = CarritoItem.objects.get(carrito=carrito, producto=producto)
        item.cantidad += 1
        item.save()
    except CarritoItem.DoesNotExist:
        item = CarritoItem.objects.create(carrito=carrito, producto=producto)
    
    return redirect('ver_carrito')

@login_required(login_url='usuarios:login')
def ver_carrito(request):
    usuario_actual = request.user
    carrito = get_object_or_404(Carrito, usuario=usuario_actual)
    items = carrito.items.all()
    return render(request, 'carrito.html', {'carrito': carrito, 'items': items})

@login_required(login_url='usuarios:login')
def eliminar_del_carrito(request, item_id):
    usuario_actual = request.user
    item = get_object_or_404(CarritoItem, id=item_id, carrito__usuario=usuario_actual)
    item.delete()
    return redirect('ver_carrito')