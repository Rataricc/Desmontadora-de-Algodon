from django.urls    import path, include
from .              import views

app_name = "tipo_alg"

urlpatterns = [
    path('Tipo_alg/', views.tipo_alg, name='tipo_alg'),
    path('Tabla_tipo_alg/', views.TablaTipoAlgodon.as_view(), name='tablatipoalgodon'),
    path('Editar_Tipo_Alg/<int:pk>/', views.EditarTablaTipoAlgodon.as_view(), name='editar_tabla_tipo_algodon'),
]