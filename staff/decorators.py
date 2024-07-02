from functools import wraps
from django.shortcuts import redirect
from usuarios.models import Usuario

def el_usuario_no_es_cliente(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('user_id'):  # Asegúrate de ajustar esto según cómo guardas la sesión
            # Obtén el usuario actual o lo que necesites para verificar el tipo de usuario
            user_id = request.session.get('user_id')
            try:
                usuario = Usuario.objects.get(rut=user_id)
                if usuario.tipo_usuario.nombre == 'Cliente':
                    return redirect('home')  # Redirige al home de clientes si es cliente
            except Usuario.DoesNotExist:
                pass  # Maneja la excepción si el usuario no existe o no se puede obtener
        else:
            return redirect('login')  # Si no hay sesión iniciada, redirige al login

        # Si no es cliente, permite el acceso a la vista
        return view_func(request, *args, **kwargs)

    return wrapper