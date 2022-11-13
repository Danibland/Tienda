from django.urls import path 
from . import views

urlpatterns = [
    path('',views.saludo, name='saludo'),
    path('nosotros',views.nosotros,name='nosotros'),
    path('productos',views.productos,name='productos')
]
