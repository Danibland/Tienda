from django.http import HttpResponse
from django.shortcuts import render
from .models import productos


# Create your views here.
def saludo(request):
    return render(request,'paginas/inicio.html')

def producto(request):
    producto = productos.objects.all()
    print(producto)
    return render(request,'productos/index.html',)

def crear_producto(request):
    return render(request,'productos/crear.html')

def editar(request):
    return render(request,'productos/editar.html')
    