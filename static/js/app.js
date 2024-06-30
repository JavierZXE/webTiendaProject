let carrito = [];

$(document).ready(function() {
  let storedCart = localStorage.getItem('carrito');
  if (storedCart) {
    carrito = JSON.parse(storedCart);
    renderCarrito();
  }

  $('.clickable').click(function() {
    let card = $(this).closest('.card');
    let producto = {
        img: card.find('.card-img-top').attr('src'),
        title: card.find('.card-title').text(),
        description: card.find('.card-text').text(),
        precio: card.find('.precio').text(),
        cantidad: card.find('.stock-quantity').text()
    };

    var newWindow = window.open('', '_blank');
    var newDocument = newWindow.document;

    var html = `
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
      <link rel="stylesheet" href="style.css">
      <link rel="stylesheet" href="demo.css">
    </head>
    <body>
      <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
          <a class="navbar-brand" href="index.html">
            <img src="assets/keloke.png" alt="imagen" class="logo">
            Tienda De Ropa
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="hombre.html">Hombre</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="mujer.html">Mujer</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="nino.html">Niño</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="producto.html">Producto</a>
              </li>
            </ul>
            <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
              <li class="nav-item pe-3">
                <a href="cuenta.html"><h2><i class="bi bi-person" style="color: black;"></i></h2></a>
              </li>
              <li class="nav-item pe-5 pt-1">
                <a href="" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight"><h4><i class="bi bi-bag" style="color: black;"></i></h4></a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div class="offcanvas-header">
          <h5 class="offcanvas-title" id="offcanvasRightLabel">Mi Compra</h5>
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          Tu Carro Esta Vacio
        </div>
      </div>
      <div class="container">
        <div class="row mt-4 mb-4">
          <div class="col">
            <h1>Producto</h1>
          </div>
          <div class="col mt-3">
            <div class="dropdown">
              <button class="btndivisa  btn btn-dark dropdown-toggle float-end me-sm-3" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Moneda CL/US
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item">USD</a></li>
                <li><a class="dropdown-item">CLP</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    <div class="container">
        <div class="row">
            <div class="col-12 col-md-6 mb-4">
                <div class="row">
                    <div class="col-12">
                        <img src="${producto.img}" class="img-fluid" alt="">
                    </div>
                </div>
            </div>
            <div class="col-12 col-md-6">
                <div class="row g-1">
                    <div class="col-12">
                        <label><h1>Marca</h1></label>
                    </div>
                    <div class="col-12">
                        <span class="demoMarca">${producto.title}</span>
                    </div>
                    <div class="col-12">
                        <label><h1>Descripcion</h1></label>
                    </div>
                    <div class="col-12">
                        <span class="demoDescripcion">${producto.description}</span>
                    </div>
                    <div class="col-12">
                        <label><h1>Precio</h1></label>
                    </div>
                    <div class="col-12">
                        <span class="precio">${producto.precio}</span>
                    </div>
                    <div class="col-12">
                        <label><h1>Stock</h1></label>
                    </div>
                    <div class="col-12">
                        <span class="demoStock">${producto.cantidad}</span>
                    </div>
                    <div class="col-12">
                        <label><h1>Talla</h1></label>
                    </div>
                    <div class="col-12">
                        <div class="btn-group" role="group" aria-label="Basic radio toggle button group">
                            <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off">
                            <label class="btn btn-outline-dark" for="btnradio1">S</label>
                          
                            <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
                            <label class="btn btn-outline-dark" for="btnradio2">M</label>
                          
                            <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
                            <label class="btn btn-outline-dark" for="btnradio3">L</label>

                            <input type="radio" class="btn-check" name="btnradio" id="btnradio4" autocomplete="off">
                            <label class="btn btn-outline-dark" for="btnradio4">XL</label>
                        </div>
                    </div>
                    <div class="col-12">
                        <button type="submit" class="agregar btn btn-dark float-end">Añadir al carro</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>
    <script src="app.js"></script>
  </body>
  </html>
  `;

    newDocument.write(html);

    newDocument.close();
  });
})

$('.agregar').click(function() {
  let card = $(this).closest('.card');
  let producto = {
    img: card.find('.card-img-top').attr('src'),
    title: card.find('.card-title').text(),
    description: card.find('.card-text').text(),
    precio: card.find('.precio').text(),
    cantidad: 1
  };
  addToCarrito(producto);
});

function addToCarrito(producto) {
  let exists = carrito.some(function(el) {
    return el.description === producto.description;
  });
  if (exists) {
    carrito.forEach(function(el) {
      if (el.description === producto.description) {
        el.cantidad++;
      }
    });
  } else {
    carrito.push(producto);
  }
  renderCarrito();
  alert("Producto agregado exitosamente")
}

function renderCarrito() {
  $('.offcanvas-body').empty();
  if (carrito.length > 0) {
    carrito.forEach(function(producto) {
      let productoDiv = `
        <div class="row mb-2">
          <div class="col-3">
            <img src="${producto.img}" class="img-fluid">
            <button type="button" class="eliminar btn btn-danger"></button>
          </div>
          <div class="col-5">
            <h6>${producto.title}</h6>
            <p>${producto.description}</p>
          </div>
          <div class="col-4"> 
            <p class="precio">${producto.precio}</p>
            <input type="number" class="cantidad" min="1" value="${producto.cantidad}" max="${producto.stock}"> 
          </div>
        </div>
      `;
      $('.offcanvas-body').append(productoDiv);
    });
    $('.eliminar').click(function() {
      let description = $(this).parent().siblings('.col-5').children('p').text();
      carrito = carrito.filter(function(el) {
        return el.description !== description;
      });
      renderCarrito();
    });
  } else {
    $('.offcanvas-body').append("<p>Tu Carro Esta Vacio</p>");
  }
}

window.addEventListener('beforeunload', function() {
  localStorage.setItem('carrito', JSON.stringify(carrito));
});

let exchangeRate;

$.getJSON('https://mindicador.cl/api', function(data) {
  exchangeRate = data.dolar.valor;
});

let preciosOriginales = [];

$('.dropdown-menu .dropdown-item').click(function() {
  let currency = $(this).text();
  
  if (currency === 'USD') {
    $('.precio').each(function() {
      let priceInPesos = Number($(this).text().replace('$', '').replace('.', ''));
      preciosOriginales.push(priceInPesos);
      
      let priceInDollars = (priceInPesos / exchangeRate).toFixed(2);
      $(this).text('$' + priceInDollars);
    });
  } else if (currency === 'CLP') {
    $('.precio').each(function(index) {
      let originalPrice = preciosOriginales[index];
      if (originalPrice) {
        $(this).text('$' + originalPrice.toLocaleString('de-DE'));
      }
    });
    preciosOriginales = [];
  }
});
