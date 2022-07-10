from django.urls import path 
from . 			 import views 

app_name = "establecimiento"

urlpatterns = [
    path('Establecimiento/', views.establecimiento, name='establecimiento'),
    path('Tabla_Establecimiento/', views.TablaEstablecimiento.as_view(), name='tablaestablecimiento'),
]