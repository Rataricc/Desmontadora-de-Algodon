from django.urls import path 
from . 			 import views 

app_name = "padron"

urlpatterns = [
    path('padron/', views.padron, name='Nuevopadron'),
    path('Tabla_Padron/', views.TablaPadron.as_view(), name='tablapadron'),
]