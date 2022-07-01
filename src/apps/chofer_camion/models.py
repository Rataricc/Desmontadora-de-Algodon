from django.db import models

from apps.padron.models import Padron

# Create your models here.

class Chofer(models.Model): 
    codigo_transportista = models.BigAutoField(auto_created=True,primary_key=True, verbose_name='ID')
    descripcion_transportista = models.CharField(max_length=30)
    carnet_conducir_chofer = models.IntegerField()
    num_cuit_chofer = models.IntegerField()
    padron = models.OneToOneField(Padron, on_delete=models.CASCADE, null=True, blank=True)

    class Meta: 
        db_table = 'chofer'

    def __str__(self):
        return self.descripcion_transportista

class Camion(models.Model): 
    chofer = models.OneToOneField(Chofer, on_delete=models.CASCADE)
    patente_camion = models.CharField(max_length=20)
    patente_acomplado = models.CharField(max_length=20)

    class Meta: 
        db_table = 'camion'

    def __str__(self): 
        return self.patente_camion + '' +self.patente_acomplado