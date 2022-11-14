from django.db import models


# Create your models here.
class productos(models.Model):
    nombre=models.CharField(max_length=30)
    stock=models.IntegerField(default=0)
    precio=models.IntegerField(default=0)
    imagen=models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True,blank=True)
    
    


