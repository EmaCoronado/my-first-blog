from django.contrib import admin
from hotel.models import Cliente, ClienteAdmin, Habitacion, HabitacionAdmin

#Registramos nuestras clases principales.
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Habitacion, HabitacionAdmin)
