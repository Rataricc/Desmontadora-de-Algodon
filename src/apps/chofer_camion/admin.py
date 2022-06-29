from django.contrib import admin
from .models import Chofer
# Register your models here.

class ChoferAdmin(admin.ModelAdmin):
    list_display = ['codigo_transportista', 'descripcion_transportista', 
        'carnet_conducir_chofer', 'num_cuit_chofer']

admin.site.register(Chofer, ChoferAdmin)