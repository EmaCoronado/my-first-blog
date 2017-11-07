from django.db import models
from django.contrib import admin

class Cliente(models.Model):
    nombre  =   models.CharField(max_length=40)
    dpi = models.IntegerField()
    nit = models.CharField(max_length=15)

    def __str__(self):

        return self.nombre

class Empleado(models.Model):
    nombre  =  models.CharField(max_length=40)
    dpi = models.IntegerField()
    nit = models.CharField(max_length=15)
    direccion = models.CharField(max_length=40)

    def __str__(self):

        return self.nombre

class Empleados(models.Model):
    nombre  =  models.CharField(max_length=40)
    dpi = models.IntegerField()
    nit = models.CharField(max_length=15)
    direccion = models.CharField(max_length=40)

    def __str__(self):

        return self.nombre


class Habitacion(models.Model):
    nombre    = models.CharField(max_length=60)
    numero      = models.IntegerField()
    clientes   = models.ManyToManyField(Cliente, through='Reservacion')

    def __str__(self):

        return self.nombre

class Reservacion(models.Model):

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

class ReservacionInLine(admin.TabularInline):

    model = Reservacion
    extra = 1

class ClienteAdmin(admin.ModelAdmin):

    inlines = (ReservacionInLine,)

class HabitacionAdmin (admin.ModelAdmin):

    inlines = (ReservacionInLine,)
