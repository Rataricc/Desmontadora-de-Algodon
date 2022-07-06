from django.contrib import admin
from .models import Establecimiento

# Register your models here.

class EstablecimientoAdmin(admin.ModelAdmin): 
    list_display = ['padron', 'codigo_establecimiento', 'descripcion_establecimiento', 'provincia', 'departamento']

admin.site.register(Establecimiento, EstablecimientoAdmin)