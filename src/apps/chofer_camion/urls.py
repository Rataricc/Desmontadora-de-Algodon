from django.urls import path 
from . 			 import views 

app_name = "chofer_camion"

urlpatterns = [
    path('Chofer/', views.chofer, name='chofer'),
    path('Camion/', views.camion, name='camion'),
    path('Tabla_Chofer/', views.TablaChofer.as_view(), name='tablachofer'),
    path('Tabla_Camion/', views.TablaCamion.as_view(), name='tablacamion'),
    path('Editar_Chofer/<int:pk>/', views.EditarTablaChofer.as_view(), name='editar_tabla_chofer'),
    path('Editar_Camion/<int:pk>/', views.EditarTablaCamion.as_view(), name='editar_tabla_camion'),
    path('Eliminar_Campo_Chofer/<int:pk>/', views.EliminarCampoChofer.as_view(), name='eliminar_campo_chofer'),
    path('Eliminar_Campo_Camion/<int:pk>/', views.EliminarCampoCamion.as_view(), name='eliminar_campo_camion'),
]