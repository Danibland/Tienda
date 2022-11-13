from django.shortcuts import render
from inventario.models import productos
from django.http import HttpResponse

# Create your views here.
def saludo(request):
    mensaje= "<h1>hola loca</h1>"
    return HttpResponse(mensaje)

def nosotros(request):
    return render(request,'paginas/nosotros.html')

def productos(request):
    return render(request,'productos/index.html')