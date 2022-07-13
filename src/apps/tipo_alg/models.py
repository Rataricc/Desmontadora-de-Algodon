from django.db import models

# Create your models here.

VARIEDAD_COSECHA = (
    ("MANUAL", "MANUAL"), 
    ("STRIPER", "STRIPER"), 
    ("USILLO", "USILLO")
)

class Tipo_Alg(models.Model): 
    descripcion_cosecha = models.CharField(max_length=20, choices=VARIEDAD_COSECHA)


    class Meta: 
        db_table = 'tipo_alg'

    def __str__(self): 
        return self.descripcion_cosecha
