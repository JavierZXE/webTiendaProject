from django.urls import path
from . import views

urlpatterns = [
    path("homeStaff", views.homeStaff, name="homeStaff"),
    path("listarCategoria", views.listarCategoria, name="listarCategoria"),
    path("listarMarca", views.listarMarca, name="listarMarca"),
    path("listarTipoUsuario", views.listarTipoUsuario, name="listarTipoUsuario"),
    path("listarFormaPago", views.listarFormaPago, name="listarFormaPago"),
    path("listarProducto", views.listarProducto, name="listarProducto"),
    path("listarUsuario", views.listarUsuario, name="listarUsuario"),
    path("guardarCategoria", views.guardarCategoria, name="guardarCategoria"),
    path("guardarMarca", views.guardarMarca, name="guardarMarca"),
    path("guardarTipoUsuario", views.guardarTipoUsuario, name="guardarTipoUsuario"),
    path("guardarFormaPago", views.guardarFormaPago, name="guardarFormaPago"),
    path("guardarProducto", views.guardarProducto, name="guardarProducto"),
    path("guardarUsuario", views.guardarUsuario, name="guardarUsuario"),
    path("buscarCategoria/<int:pk>", views.buscarCategoria, name="buscarCategoria"),
    path("buscarMarca/<int:pk>", views.buscarMarca, name="buscarMarca"),
    path("buscarTipoUsuario/<int:pk>", views.buscarTipoUsuario, name="buscarTipoUsuario"),
    path("buscarFormaPago/<int:pk>", views.buscarFormaPago, name="buscarFormaPago"),
    path("buscarProducto/<int:pk>", views.buscarProducto, name="buscarProducto"),
    path("buscarUsuario/<str:pk>", views.buscarUsuario, name="buscarUsuario"),
    path("eliminarCategoria/<int:pk>", views.eliminarCategoria, name="eliminarCategoria"),
    path("eliminarMarca/<int:pk>", views.eliminarMarca, name="eliminarMarca"),
    path("eliminarTipoUsuario/<int:pk>", views.eliminarTipoUsuario, name="eliminarTipoUsuario"),
    path("eliminarFormaPago/<int:pk>", views.eliminarFormaPago, name="eliminarFormaPago"),
    path("eliminarProducto/<int:pk>", views.eliminarProducto, name="eliminarProducto"),
    path("eliminarUsuario/<str:pk>", views.eliminarUsuario, name="eliminarUsuario")
]