from django.contrib import admin
from .models        import Variedad

# Register your models here.

class VariedadAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion_variedad']

admin.site.register(Variedad, VariedadAdmin)
