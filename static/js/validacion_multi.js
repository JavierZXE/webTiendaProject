document.addEventListener('DOMContentLoaded', function() {
    var formulario = document.getElementById('usuarioForm');
    if (formulario) {
        formulario.addEventListener('submit', function(event) {
            var nombre = document.getElementById('inputNombre').value;
            var mensaje = '';

            if (!nombre) {
                mensaje += 'Nombre es obligatorio.\n';
            }

            if (mensaje) {
                alert(mensaje);
                event.preventDefault();
            }
        });
    }
});