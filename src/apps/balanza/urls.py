from django.urls import path 
from . 			 import views 

app_name = "balanza"

urlpatterns = [
    path('Balanza/', views.balanza, name='balanza'),
    path('Tabla_Balanza/', views.TablaBalanza.as_view(), name='tablabalanza'),
    path('Editar_tabla/<int:pk>/', views.EditarTabla.as_view(), name='editar_tabla_balanza'),
    path('Eliminar_Campo/<int:pk>/', views.EliminarCampoBalanza.as_view(), name='eliminar_campo_balanza'),
]