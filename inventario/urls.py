from django.urls import path 
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static 
from django.urls import include 

urlpatterns = [
    path('',views.producto, name='productos'),
    path('productos',views.producto,name='productos'),
    path('crear',views.crear_producto,name='crear'),
    path('editar',views.editar,name='editar'),
    path('login',views.login, name='login'),
    path('accounts/',include('django.contrib.auth.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
