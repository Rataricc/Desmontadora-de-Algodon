from django.urls import path 
from . 			 import views 

app_name = "variedad"

urlpatterns = [
    path('Variedad/', views.variedad, name='variedad'),
    path('Tabla_Variedad/', views.TablaVariedad.as_view(), name='tablavariedad'),
    path('Editar_Variedad/<int:pk>/', views.EditarTablaVariedad.as_view(), name='editar_tabla_variedad_semilla'),
    path('Eliminar_Campo_Variedad/<int:pk>/', views.EliminarCampoVariedad.as_view(), name='eliminar_campo_variedad'),
]