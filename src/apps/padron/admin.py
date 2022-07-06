from django.contrib import admin
from .models        import Padron
# Register your models here.

class PadronAdmin(admin.ModelAdmin): 
    list_display = ['codigo_cliente', 'nombre_completoApellidos', 'chofer']

admin.site.register(Padron, PadronAdmin)
