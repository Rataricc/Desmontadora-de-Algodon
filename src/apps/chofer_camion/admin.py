from django.contrib import admin
from .models import Chofer, Camion
# Register your models here.

class ChoferAdmin(admin.ModelAdmin):
    list_display = ['codigo_transportista', 'descripcion_transportista', 'carnet_conducir_chofer', 'num_cuit_chofer']

admin.site.register(Chofer, ChoferAdmin)

class CamionAdmin(admin.ModelAdmin): 
    list_display = ['chofer', 'patente_camion', 'patente_acomplado']

admin.site.register(Camion, CamionAdmin)