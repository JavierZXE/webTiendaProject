document.addEventListener('DOMContentLoaded', function() {
    var formulario = document.getElementById('usuarioForm');
    if (formulario) {
        formulario.addEventListener('submit', function(event) {
            event.preventDefault();

            var rut = document.getElementById('inputRut').value;
            var nombre = document.getElementById('inputNombre').value;
            var apellido = document.getElementById('inputApellido').value;
            var correo = document.getElementById('inputEmail').value;
            var region = document.getElementById('inputRegion').value;
            var fecha_nacimiento = document.getElementById('inputFechanacimiento').value;
            var tipo_usuario = document.getElementById('inputTipoUsuario').value;
            var educacion = document.getElementById('inputEducacion').value;
            var contrasenna = document.getElementById('inputContrasenna').value;

            var mensaje = '';

            if (!rut) {
                mensaje += 'Rut es obligatorio.\n';
            }

            if (!nombre) {
                mensaje += 'Nombre es obligatorio.\n';
            }

            if (!apellido) {
                mensaje += 'Apellido es obligatorio.\n';
            }

            if (!correo) {
                mensaje += 'Email es obligatorio.\n';
            }

            if (!region || region === 'Elige...') {
                mensaje += 'Debe seleccionar una región.\n';
            }

            if (!fecha_nacimiento) {
                mensaje += 'Fecha de nacimiento es obligatoria.\n';
            }

            if (!tipo_usuario || tipo_usuario === 'Elige...') {
                mensaje += 'Debe seleccionar un tipo de usuario.\n';
            }

            if (!educacion || educacion === 'Elige...') {
                mensaje += 'Debe seleccionar un grado de educación.\n';
            }

            if (!contrasenna) {
                mensaje += 'Contraseña es obligatoria.\n';
            }

            if (mensaje) {
                alert(mensaje);
                return false;
            }

            this.submit();
        });
    }
});