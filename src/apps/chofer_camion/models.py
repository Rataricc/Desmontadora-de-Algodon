from django.db import models

# Create your models here.

class Chofer(models.Model): 
    codigo_transportista = models.IntegerField(max_length=6, primary_key=True)
    descripcion_transportista = models.CharField(max_length=30)
    carnet_conducir_chofer = models.IntegerField(max_length=15)
    num_cuit_chofer = models.IntegerField(max_length=11)

    class Meta: 
        db_table = 'chofer'

    def __str__(self):
        return self.codigo_transportista, self.descripcion_transportista, self.carnet_conducir_chofer, self.num_cuit_chofer