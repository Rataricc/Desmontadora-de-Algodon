from django.urls import path 
from . 			 import views 

app_name = "lotes"

urlpatterns = [
    path('lotes/', views.lotes, name='nuevolote'),
]