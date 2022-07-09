from django.urls import path 
from . 			 import views 

app_name = "balanza"

urlpatterns = [
    path('Balanza/', views.balanza, name='balanza'),
]