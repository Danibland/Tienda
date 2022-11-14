from django.urls import path 
from . import views

urlpatterns = [
    path('',views.saludo, name='saludo'),
    path('productos',views.producto,name='productos'),
    path('productos/crear',views.crear_producto,name='crear'),
    path('productos/editar',views.editar,name='editar')
]
