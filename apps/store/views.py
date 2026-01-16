from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        'title': 'Tienda',
    }
    return render(request, 'store/index.html', context)

def create(request):
  
    form = Telefono()
    form.nombre = request.POST['nombre']
    form.marca = request.POST['marca']
    form.procesador = request.POST['procesador']
    form.rom = request.POST['rom']
    form.ram = request.POST['ram']
    form.save()
    
    context = {
        'titulo': 'Respuesta',
        'form': form, 
    }
    return render(request, 'empleado/cellphones.html', context)
  