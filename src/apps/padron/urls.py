from django.urls import path 
from . 			 import views 

app_name = "padron"

urlpatterns = [
    path('padron/', views.padron, name='Nuevopadron'),
    path('Tabla_Padron/', views.TablaPadron.as_view(), name='tablapadron'),
    path('Editar_Padron/<int:pk>/', views.EditarTablaPadron.as_view(), name='editar_tabla_padron'),
    path('Eliminar_Campo_Padron/<int:pk>/', views.EliminarCampoPadron.as_view(), name='eliminar_campo_padron'),
]