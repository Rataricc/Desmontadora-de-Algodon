from django.contrib import admin
from .models import Lotes
# Register your models here.

class LotesAdmin(admin.ModelAdmin): 
    list_display = ['padron', 'establecimiento', 'numero_lote']

admin.site.register(Lotes, LotesAdmin)