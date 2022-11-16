from django.http import HttpResponse
from django.shortcuts import render,redirect
from inventario.models import productos
from .forms import productos_form
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def saludo(request):
    return render(request,'paginas/inicio.html')

def producto(request):
    producto=productos.objects.all()
    return render(request,'productos/index.html',{'producto':producto})

def crear_producto(request):
    formulario=productos_form(request.POST or None, request.FILES or None)
    
    if formulario.is_valid():
        formulario.save()
        return redirect('producto')
    
    return render(request,'productos/crear.html', {'formulario':formulario})

def editar(request):
    return render(request,'productos/editar.html')

"""def editar(request):
    if request.method=="POST":
        subject=request.POST['asunto']
        
        message=request.POST['mensaje']+ "Remitente "+ request.POST['correo']
        email_from=settings.EMAIL_HOST_USER
        recipent_list=[""]
        send_mail(subject, message, email_from, recipent_list)
        return redirect('editar.html')
    
    return   render(request,"editar.html")  """