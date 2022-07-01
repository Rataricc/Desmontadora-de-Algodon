from django.contrib import admin
from .models        import Padron, Establecimiento, Lotes
# Register your models here.

class PadronAdmin(admin.ModelAdmin): 
    list_display = ['codigo_cliente', 'nombre_completoApellidos', 'chofer']

admin.site.register(Padron, PadronAdmin)

class EstablecimientoAdmin(admin .ModelAdmin): 
    list_display = ['padron', 'codigo_establecimiento' , 'descripcion_establecimiento', 'provincia', 'departamento']

admin.site.register(Establecimiento, EstablecimientoAdmin)

class LotesAdmin(admin.ModelAdmin): 
    list_display = ['padron', 'establecimiento', 'numero_lote']

admin.site.register(Lotes, LotesAdmin)