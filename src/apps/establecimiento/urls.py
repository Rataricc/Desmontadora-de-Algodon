from django.urls import path 
from . 			 import views 

app_name = "establecimiento"

urlpatterns = [
    path('Establecimiento/', views.establecimiento, name='establecimiento'),
    path('Tabla_Establecimiento/', views.TablaEstablecimiento.as_view(), name='tablaestablecimiento'),
    path('Editar_Establecimiento/<int:pk>/', views.EditarTablaEstablecimiento.as_view(), name='editar_tabla_establecimiento'),
    path('Eliminar_Campo_Establecimiento/<int:pk>/', views.EliminarCampoEstablecimiento.as_view(), name='eliminar_campo_establecimiento'),
]