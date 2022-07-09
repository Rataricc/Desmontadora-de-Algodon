from django.urls import path 
from . 			 import views 

app_name = "variedad"

urlpatterns = [
    path('Variedad/', views.variedad, name='variedad'),
]