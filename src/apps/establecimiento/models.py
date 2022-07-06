from django.db          import models
from apps.padron.models import Padron
# Create your models here.


class Establecimiento(models.Model): 
    padron = models.ForeignKey(Padron, on_delete=models.CASCADE)
    codigo_establecimiento = models.BigAutoField(auto_created=True, primary_key=True, unique=True, verbose_name='ID')
    descripcion_establecimiento = models.CharField(max_length=30)
    provincia = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)

    class Meta: 
        db_table = 'establecimiento'

    def __str__(self): 
        return self.descripcion_establecimiento + '' + self.provincia + '' + self.departamento