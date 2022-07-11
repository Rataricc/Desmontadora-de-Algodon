from django.contrib.auth.models import AbstractUser
from django.db                  import models

# Create your models here.

class Usuario(AbstractUser): 
    apodo = models.CharField(max_length=20, null=True, blank=True, verbose_name='apodo usuario')
    fecha_nacimiento = models.DateField(null=True, blank=True, verbose_name='fecha de nacimiento usuario')
    direccion_domicilio = models.CharField(max_length=60, null=True, blank=True, verbose_name='direccion domicilio usuario')
    class Meta: 
        db_table = 'usuarios'
