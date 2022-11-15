from django.db import models


# Create your models here.
class productos(models.Model):
    nombre=models.CharField(max_length=30)
    imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    precio=models.IntegerField(default=0)
   
    
    


