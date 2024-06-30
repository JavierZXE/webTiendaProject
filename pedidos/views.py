from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Carrito, Usuario, FormaPago
# Create your views here.
'''
def crear_pedido(request):
    carrito = get_object_or_404(Carrito, usuario=request.user)
    if request.method == 'POST':
        forma_pago_id = request.POST.get('pago')
        forma_pago = get_object_or_404(FormaPago, id=forma_pago_id, activo=True)
        pedido = Pedido.objects.create(
            usuario=request.user,
            carrito=carrito,
            total=carrito.get_total(),
            pago=forma_pago
        )
        carrito.completado = True
        carrito.save()
        return redirect('detalle_pedido', pedido_id=pedido.id)
    else:
        formas_pago = FormaPago.objects.filter(activo=True)
        return render(request, 'crear_pedido.html', {'formas_pago': formas_pago})
'''