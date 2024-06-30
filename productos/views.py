from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def mujer(request):
    return render(request, "mujer.html")

def hombre(request):
    return render(request, "hombre.html")

def ninno(request):
    return render(request, "ninno.html")