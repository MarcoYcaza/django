from django.db import models
from apps.lectores.models import Lector

class Libro (models.Model):

    name = models.CharField(max_length=50,verbose_name='Nombre')
    author = models.CharField(max_length=50,verbose_name='autor')
    year= models.CharField(max_length=50,verbose_name='año')

    user = models.ForeignKey(Lector,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

