from django.urls import path 
from . 			 import views 

app_name = "chofer_camion"

urlpatterns = [
    path('Chofer/', views.chofer, name='chofer'),
    path('Camion/', views.camion, name='camion'),
]