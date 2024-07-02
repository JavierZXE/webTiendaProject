from django.shortcuts import render, redirect, get_object_or_404
from usuarios.models import TipoDeUsuario
from productos.models import Marca, Categoria, Producto
from usuarios.models import Usuario
from pedidos.models import FormaPago
from django.contrib.auth.decorators import login_required
from .decorators import el_usuario_no_es_cliente
from datetime import datetime

# Create your views here.
@el_usuario_no_es_cliente
@login_required(login_url='login')
def homeStaff(request):
    return render(request, "home_staff.html")

@el_usuario_no_es_cliente
@login_required(login_url='login')
def listarCategoria(request):
    listado = Categoria.objects.all()
    context = {"listado": listado}
    return render(request, "listarCategoria.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def guardarCategoria(request):
    context = {}

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST

        if 'btnGuardar' in request.POST:

            if id== '0':
                Categoria.objects.create(nombre=nombre, activo=activo)
                return redirect('listarCategoria')
            else:
                item = Categoria()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                return redirect('listarCategoria')
            
    return render(request, "guardarCategoria.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def buscarCategoria(request, pk):
    context = {}
    try:
        item = Categoria.objects.get(pk=pk)
        context['item'] = item
    except:
        context['error'] = 'Elemento seleccionado no encontrado'
        
    return render(request, "guardarCategoria.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def eliminarCategoria(request, pk):
    context = {}
    error = ''
    exito = ''

    try:
        item = Categoria.objects.get(pk=pk)
        item.delete()
        exito = 'El tipo de usuario fue eliminado'
    except:
        error = 'El item no fue encontrado'
    
    listado = Categoria.objects.all()
    context = {'listado': listado, 'exito': exito, 'error': error}
    
    return render(request, "listarCategoria.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def listarMarca(request):
    listado = Marca.objects.all()
    context = {"listado": listado}
    return render(request, "listarMarca.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def guardarMarca(request):
    context = {}

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST

        if 'btnGuardar' in request.POST:

            if id== '0':
                Marca.objects.create(nombre=nombre, activo=activo)
                return redirect('listarMarca')
            else:
                item = Marca()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                return redirect('listarMarca')
            
    return render(request, "guardarMarca.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def buscarMarca(request, pk):
    context = {}
    try:
        item = Marca.objects.get(pk=pk)
        context['item'] = item
    except:
        context['error'] = 'Elemento seleccionado no encontrado'
    return render(request, "guardarMarca.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def eliminarMarca(request, pk):
    context = {}
    error = ''
    exito = ''

    try:
        item = Marca.objects.get(pk=pk)
        item.delete()
        exito = 'El tipo de usuario fue eliminado'
    except:
        error = 'El item no fue encontrado'
    
    listado = Marca.objects.all()
    context = {'listado': listado, 'exito': exito, 'error': error}
    
    return render(request, "listarMarca.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def listarTipoUsuario(request):
    listado = TipoDeUsuario.objects.all()
    context = {"listado": listado}
    return render(request, "listarTipoUsuario.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def buscarTipoUsuario(request, pk):
    context = {}
    try:
        item = TipoDeUsuario.objects.get(pk=pk)
        context['item'] = item
    except:
        context['error'] = 'Elemento seleccionado no encontrado'

    return render(request, "guardarTipoUsuario.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def eliminarTipoUsuario(request, pk):
    context = {}
    error = ''
    exito = ''

    try:
        item = TipoDeUsuario.objects.get(pk=pk)
        item.delete()
        exito = 'El tipo de usuario fue eliminado'
    except:
        error = 'El item no fue encontrado'
    
    listado = TipoDeUsuario.objects.all()
    context = {'listado': listado, 'exito': exito, 'error': error}
    return render(request, 'listarTipoUsuario.html', context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def guardarTipoUsuario(request):
    context = {}

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST

        if 'btnGuardar' in request.POST:

            if id== '0':
                TipoDeUsuario.objects.create(nombre=nombre, activo=activo)
                return redirect('listarTipoUsuario')
            else:
                item = TipoDeUsuario()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                return redirect('listarTipoUsuario')

    return render(request, "guardarTipoUsuario.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def listarFormaPago(request):
    listado = FormaPago.objects.all()
    context = {"listado":listado}
    return render(request, "listarFormaPago.html",context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def guardarFormaPago(request):
    context = {}

    if request.method == 'POST':
        id = request.POST['txtId']
        nombre = request.POST['txtNombre']
        activo = 'chkActivo' in request.POST

        if 'btnGuardar' in request.POST:

            if id== '0':
                FormaPago.objects.create(nombre=nombre, activo=activo)
                return redirect('listarFormaPago')
            else:
                item = FormaPago()
                item.id = id
                item.nombre = nombre
                item.activo = activo
                item.save()
                return redirect('listarFormaPago')
            
    return render(request, "guardarFormaPago.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def buscarFormaPago(request, pk):
    context = {}
    try:
        item = FormaPago.objects.get(pk=pk)
        context['item'] = item
    except:
        context['error'] = 'Elemento seleccionado no encontrado'
        
    return render(request, "guardarFormaPago.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def eliminarFormaPago(request, pk):
    context = {}
    error = ''
    exito = ''

    try:
        item = FormaPago.objects.get(pk=pk)
        item.delete()
        exito = 'El tipo de usuario fue eliminado'
    except:
        error = 'El item no fue encontrado'
    
    listado = FormaPago.objects.all()
    context = {'listado': listado, 'exito': exito, 'error': error}
    
    return render(request, "listarFormaPago.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def listarUsuario(request):
    listado = Usuario.objects.all()
    context = {"listado":listado}
    return render(request, "listarUsuario.html",context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def guardarUsuario(request):
    tipousuario = TipoDeUsuario.objects.filter(activo=True)
    context = {"tipousuario": tipousuario}
    
    if request.method == 'POST':
        rut = request.POST['txtRut']
        nombre = request.POST['txtNombre']
        apellido = request.POST['txtApellido']
        correo = request.POST['txtCorreo']
        region = request.POST['txtRegion']
        fecha_nacimiento = request.POST['txtFecha_nacimiento']
        tipo_usuario_id = request.POST['txtTipo_usuario']
        educacion = request.POST['txtEducacion']
        contrasenna = request.POST['txtContrasenna']
        
        tipo_usuario = TipoDeUsuario.objects.get(pk=tipo_usuario_id)
        
        try:
            usuario = Usuario.objects.get(rut=rut)
            usuario.nombre = nombre
            usuario.apellido = apellido
            usuario.correo = correo
            usuario.region = region
            usuario.fecha_nacimiento = fecha_nacimiento
            usuario.tipo_usuario = tipo_usuario
            usuario.educacion = educacion
            usuario.contrasenna = contrasenna
            usuario.save()
        except Usuario.DoesNotExist:
            Usuario.objects.create(
                rut=rut,
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                region=region,
                fecha_nacimiento=fecha_nacimiento,
                contrasenna=contrasenna,
                tipo_usuario=tipo_usuario,
                educacion=educacion
            )
        return redirect('listarUsuario')
    
    return render(request, "guardarUsuario.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def buscarUsuario(request, pk):
    item = get_object_or_404(Usuario, rut=pk)
    tipousuario = TipoDeUsuario.objects.filter(activo=True)
    
    context = {
        'item': item,
        'tipousuario': tipousuario,
        'tipo_usuario_id': item.tipo_usuario.id,
        'region': item.region,
        'fecha_nacimiento': item.fecha_nacimiento.strftime("%Y-%m-%d") if item.fecha_nacimiento else '',
        'educacion': item.educacion
    }
    return render(request, "guardarUsuario.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def eliminarUsuario(request, pk):
    context = {}
    error = ''
    exito = ''

    try:
        item = Usuario.objects.get(rut=pk)
        item.delete()
        exito = 'El usuario fue eliminado'
    except:
        error = 'El no fue encontrado'
    
    listado = Usuario.objects.all()
    context = {'listado': listado, 'exito': exito, 'error': error}
    
    return render(request, "listarUsuario.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def listarProducto(request):
    listado = Producto.objects.all()
    context = {"listado":listado}
    return render(request, "listarProducto.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def guardarProducto(request):
    marcas = Marca.objects.filter(activo=True)
    categorias = Categoria.objects.filter(activo=True)
    context = {"marcas":marcas,
               "categorias":categorias}
    
    if request.method == 'POST':
        id = request.POST['txtId']
        categoria_id = request.POST['txtCategoria']
        marca_id = request.POST['txtMarca']
        descripcion = request.POST['txtDescripcion']
        precio = request.POST['txtPrecio']
        stock = request.POST['txtStock']
        barcode = request.POST['txtBarcode']
        
        categoria = Categoria.objects.get(pk=categoria_id)
        marca = Marca.objects.get(pk=marca_id)
        
        if id== '0':
                Producto.objects.create(
                    categoria=categoria,
                    imagen=request.FILES['txtImagen'],
                    marca=marca,
                    descripcion=descripcion,
                    precio=precio,
                    stock=stock,
                )
                return redirect('listarProducto')
        else:
            item = Producto.objects.get(pk=id)
            item.categoria = categoria
            if 'txtImagen' in request.FILES:
                item.imagen = request.FILES['txtImagen']
            item.marca = marca
            item.descripcion = descripcion
            item.precio = precio
            item.stock = stock
            item.barcode = barcode
            item.save()
            return redirect('listarProducto')

            
    
    return render(request, "guardarProducto.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def buscarProducto(request, pk):
    context = {}
    try:
        item = Producto.objects.get(pk=pk)
        context['item'] = item
        context['categorias'] = Categoria.objects.filter(activo=True)
        context['marcas'] = Marca.objects.filter(activo=True)
        context['categoria_id_seleccionada'] = item.categoria.id
        context['marca_id_seleccionada'] = item.marca.id
    except Producto.DoesNotExist:
        context['error'] = 'Elemento seleccionado no encontrado'
        
    return render(request, "guardarProducto.html", context)

@el_usuario_no_es_cliente
@login_required(login_url='login')
def eliminarProducto(request, pk):
    context = {}
    error = ''
    exito = ''

    try:
        item = Producto.objects.get(pk=pk)
        item.delete()
        exito = 'El tipo de usuario fue eliminado'
    except:
        error = 'El item no fue encontrado'
    
    listado = Producto.objects.all()
    context = {'listado': listado, 'exito': exito, 'error': error}
    return render(request, "listarProducto.html", context)
