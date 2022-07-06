from django.db import models
#import uuid
#from apps.padron.utils import custom_id


# Create your models here.

class Padron(models.Model):
    codigo_cliente = models.BigAutoField(auto_created=True, primary_key=True, unique=True, verbose_name='ID')
    nombre_completoApellidos = models.CharField(max_length=50)
    
    class Meta: 
        db_table = 'padron'

    def __str__(self):
        return self.nombre_completoApellidos
 