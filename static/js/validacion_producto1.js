document.addEventListener('DOMContentLoaded', function() {

    var inputImagen = document.getElementById('inputImagen');
    var vistaPreviaImagen = document.getElementById('vistaPreviaImagen');

    if (inputImagen && vistaPreviaImagen) {
        inputImagen.addEventListener('change', function(event) {
            var archivo = inputImagen.files[0];
            if (archivo) {
                vistaPreviaImagen.src = URL.createObjectURL(archivo);
            } else {
                vistaPreviaImagen.src = "{% if item.imagen %}{{ item.imagen.url }}{% endif %}";
            }
        });
    }


    var formulario = document.getElementById('productoForm');
    if (formulario) {
        formulario.addEventListener('submit', function(event) {
            event.preventDefault();

            var categoria = document.getElementById('inputCategoria').value;
            var imagen = document.getElementById('inputImagen').value;
            var marca = document.getElementById('inputMarca').value;
            var descripcion = document.getElementById('inputDescripcion').value;
            var precio = document.getElementById('inputPrecio').value;
            var stock = document.getElementById('inputStock').value;

            var mensaje = '';

            if (!categoria || categoria === 'Elige...') {
                mensaje += 'Debe seleccionar una categoría.\n';
            }

            if (!marca || marca === 'Elige...') {
                mensaje += 'Debe seleccionar una marca.\n';
            }

            if (!descripcion) {
                mensaje += 'Descripción es obligatoria.\n';
            }

            if (!precio) {
                mensaje += 'Precio es obligatorio.\n';
            }

            if (!stock) {
                mensaje += 'Stock es obligatorio.\n';
            }

            if (mensaje) {
                alert(mensaje);
                return false;
            }

            this.submit();
        });
    }
});
