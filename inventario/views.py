from django.http import HttpResponse
from django.shortcuts import render
from inventario.models import productos
from .forms import productos_form

# Create your views here.
def saludo(request):
    return render(request,'paginas/inicio.html')

def producto(request):
    producto=productos.objects.all()
    return render(request,'productos/index.html',{'producto':producto})

def crear_producto(request):
    formulario=productos_form(request.POST or None)
    return render(request,'productos/crear.html',{'formulario': formulario})

def editar(request):
    return render(request,'productos/editar.html')
    