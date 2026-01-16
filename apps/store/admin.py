from django.contrib import admin
from .models import Empleado, Telefono, TelefonoComponente

admin.site.register(Empleado)
admin.site.register(Telefono)
admin.site.register(TelefonoComponente)