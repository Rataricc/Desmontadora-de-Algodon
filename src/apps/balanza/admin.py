from django.contrib import admin
from .models        import Balanza

# Register your models here.

class BalanzaAdmin(admin.ModelAdmin): 
    list_display = ['numero_remito', 'padron', 'codigo_productor', 'tipo_alg', 'establecimiento', 'lotes', 'variedad', 'chofer', 'cuit_chofer',
    'patente_camion', 'patente_acoplado', 'fecha_actual']

admin.site.register(Balanza, BalanzaAdmin)
"""
    NO SE REALIZO NINGUN MAKEMIGRATIONS AUN - NI TAMPOCO UN MIGARTE DE ESTA TABLA.
"""