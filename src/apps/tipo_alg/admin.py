from django.contrib import admin
from .models        import Tipo_Alg
# Register your models here.

class Tipo_algAdmin(admin.ModelAdmin): 
    list_display = ['id', 'descripcion_cosecha']

admin.site.register(Tipo_Alg, Tipo_algAdmin)