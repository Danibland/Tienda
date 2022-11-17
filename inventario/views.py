from django.http import HttpResponse
from django.shortcuts import render,redirect
from inventario.models import productos
from .forms import productos_form
from django.views import View 
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


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

def send_email(nombre, correo, direccion, ciudad, tel):
    contexto = {'nombre': nombre, 'direccion': direccion, 'ciudad': ciudad, 'tel': tel}
    
    template = get_template('correo.html')
    content = template.render(contexto)
    
    email = EmailMultiAlternatives(
        'Titulo cacorreo',
        'cuerpo cacorreo',
        settings.EMAIL_HOST_USER,
        [correo]
    )
    
    email.attach_alternative(content, 'text/html')
    email.send()
    print('envió el cacorreo')

def editar(request):
    
    if request.method=='POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        tel = request.POST.get('tel')
        send_email(nombre, email, direccion, ciudad, tel)
    
    return render(request,'productos/editar.html')


