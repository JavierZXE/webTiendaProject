from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password, check_password
from .models import Usuario, TipoDeUsuario
from django.contrib import messages


# Create your views here.
def registration(request):
    if request.method == 'POST':
        
        rut = request.POST['rut']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo = request.POST['correo']
        region = request.POST['region']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        educacion = request.POST['educacion']
        contrasenna = request.POST['contrasenna']
        
        try:
            tipo_usuario_cliente = TipoDeUsuario.objects.get(nombre='Cliente')
        except TipoDeUsuario.DoesNotExist:
            messages.error(request, 'El tipo de usuario "Cliente" no existe.')
            return redirect('registration')
        
        usuario = Usuario(
            rut=rut,
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            region=region,
            fecha_nacimiento=fecha_nacimiento,
            tipo_usuario= tipo_usuario_cliente,
            educacion=educacion,
            contrasenna=contrasenna
        )

        usuario.save()
        return redirect('login')

    today = datetime.today()
    eighteen_years_ago = today - timedelta(days=18*365 + 5)
    max_date = eighteen_years_ago.strftime('%Y-%m-%d')
    return render(request, 'registration.html', {'max_date': max_date})

def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contrasenna = request.POST.get('contrasenna')
        
        try:
            usuario = Usuario.objects.get(correo=correo)
            if check_password(contrasenna, usuario.contrasenna):
                request.session['user_id'] = usuario.rut
                if usuario.tipo_usuario.nombre == 'Cliente':
                    return redirect('home')
                else:
                    return redirect('homeStaff')
            else:
                messages.error(request, 'Contraseña incorrecta')
        
        except Usuario.DoesNotExist:
            messages.error(request, 'El usuario no existe')
            
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return render(request, "home.html")