from django.db import models

# Create your models here.

class Padron(models.Model):
    nombre_completo_apellidos = models.CharField(max_length=50)

    class Meta: 
        db_table = 'padron'

    def __str__(self):
        return self.nombre_completo_apellidos