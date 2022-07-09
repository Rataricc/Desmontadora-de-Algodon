from django.urls    import path, include
from .              import views

app_name = "tipo_alg"

urlpatterns = [
    path('Tipo_alg/', views.tipo_alg, name='tipo_alg'),
]