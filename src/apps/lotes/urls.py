from django.urls import path 
from . 			 import views 

app_name = "lotes"

urlpatterns = [
    path('lotes/', views.lotes, name='nuevolote'),
    path('Tabla_Lotes/', views.TablaLotes.as_view(), name='tablalotes'),
    path('Editar_Lotes/<int:pk>/', views.EditarTablaLotes.as_view(), name='editar_tabla_lotes'),
]