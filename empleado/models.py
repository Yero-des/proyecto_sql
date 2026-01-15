from django.db import models

# Creamos los modelos.
class Empleado(models.Model):
    nombre = models.CharField(max_length=15, verbose_name='Nombre')
    apellido = models.CharField(max_length=25, verbose_name='Apellido')
    correo = models.EmailField(unique=True, max_length=60, verbose_name='Correo')
    edad = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nombre
        
class Telefono(models.Model):
    modelo = models.CharField(max_length=25)
    marca = models.CharField(max_length=25)
    procesador = models.CharField(max_length=25)
    rom = models.IntegerField()
    ram = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.modelo} - {self.marca}'
        
class TelefonoComponente(models.Model):
    telefono = models.OneToOneField(Telefono, on_delete=models.CASCADE, related_name='componente')
    buetooth = models.BooleanField()
    wifi = models.BooleanField()
    camera = models.BooleanField()
        
        
        
        
        
        
        
        