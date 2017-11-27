from django.db import models
from django.utils import timezone
# Create your models here.
class Productos(models.Model):
	nombre=models.CharField(max_length=100)
	precio=models.IntegerField(null=True, blank=True)
	descripcion=models.TextField()
	imagen=models.ImageField(upload_to='imagenes')


	def __str__(self):
		return self.nombre