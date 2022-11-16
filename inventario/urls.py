from django.urls import path 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('',views.saludo, name='saludo'),
    path('productos',views.producto,name='productos'),
    path('productos/crear',views.crear_producto,name='crear'),
    path('productos/editar',views.editar,name='editar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
