from django.contrib import admin
from .models        import Padron
# Register your models here.

class PadronAdmin(admin.ModelAdmin): 
    list_display = ['id', 'nombre_completo_apellidos']

admin.site.register(Padron, PadronAdmin)