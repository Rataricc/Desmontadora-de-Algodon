from django.db import models

# Create your models here.

class Tipo_Alg(models.Model): 
    descripcion_cosecha = models.CharField(max_length=20)


    class Meta: 
        db_table = 'tipo_alg'

    def __str__(self): 
        return self.descripcion_cosecha
