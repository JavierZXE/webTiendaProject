from django.urls import path
from . import views

urlpatterns = [
    path("productonuevo", views.productonuevo, name="productonuevo"),
]