from apps.establecimiento.models import Establecimiento
from apps.padron.models          import Padron
from django.db                   import models


# Create your models here.

class Lotes(models.Model): 
    padron = models.ForeignKey(Padron, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    numero_lote = models.BigAutoField(auto_created=True, primary_key=True, unique=True, verbose_name='ID')

    class Meta: 
        db_table = 'lotes'

    def __str__(self):
        return '%s' % (self.numero_lote)