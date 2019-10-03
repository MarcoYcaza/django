from django.db import models


class Lector(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellido')
    address = models.CharField(max_length=50, verbose_name='Direccion')
    email = models.EmailField(max_length=50, verbose_name='Correo')
    bdate = models.DateField(verbose_name='Fecha de nacimiento')

    def __str__(self):
        return str(self.name)


class Preferencia(models.Model):
    fk = models.ForeignKey(Lector, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, verbose_name='Titulo')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return str(self.name)
