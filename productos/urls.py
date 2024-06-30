from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hombre", views.hombre, name="hombre"),
    path("mujer", views.mujer, name="mujer"),
    path("ninno", views.ninno, name="ninno")
]