from django.urls import path 
from . 			 import views 

app_name = "balanza"

urlpatterns = [
    path('Balanza/', views.balanza, name='balanza'),
    path('Tabla_Balanza/', views.TablaBalanza.as_view(), name='tablabalanza'),
]