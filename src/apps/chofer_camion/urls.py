from django.urls import path 
from . 			 import views 

app_name = "chofer_camion"

urlpatterns = [
    path('Chofer/', views.chofer, name='chofer'),
    path('Camion/', views.camion, name='camion'),
    path('Tabla_Chofer/', views.TablaChofer.as_view(), name='tablachofer'),
    path('Tabla_Camion/', views.TablaCamion.as_view(), name='tablacamion'),
    path('Editar_Chofer/<int:pk>/', views.EditarTablaChofer.as_view(), name='editar_tabla_chofer'),
]