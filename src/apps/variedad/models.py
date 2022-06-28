from django.db import models

# Create your models here.

class Variedad(models.Model): 
    descripcion_variedad = models.CharField(max_length=20)

    class Meta: 
        db_table = 'variedad'

    def __str__(self): 
        return self.descripcion_variedad