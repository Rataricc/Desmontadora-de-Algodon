from apps.establecimiento.models import Establecimiento
from apps.chofer_camion.models   import Chofer
from apps.tipo_alg.models        import Tipo_Alg
from apps.variedad.models        import Variedad
from apps.padron.models          import Padron
from apps.lotes.models           import Lotes
from django.db                   import models


# Create your models here.

class Balanza(models.Model): 
    # Al numero de remito: falta agregar una funcionalidad, espero que funcione.
    numero_remito = models.CharField(max_length=12, primary_key=True, unique=True, editable=False, verbose_name='ID') 
    padron = models.ForeignKey(Padron, on_delete=models.CASCADE, verbose_name='codigo_cliente')
    codigo_productor = models.BigIntegerField(unique=True)
    tipo_alg = models.ForeignKey(Tipo_Alg, on_delete=models.CASCADE, verbose_name='codigo_cosecha')
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, verbose_name='codigo_establecimiento')
    lotes = models.ForeignKey(Lotes, on_delete=models.CASCADE, verbose_name='numero_lote')
    variedad = models.ForeignKey(Variedad, on_delete=models.CASCADE, verbose_name='codigo_variedadSemilla')
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE, verbose_name='codigo_transportista')
    cuit_chofer = models.IntegerField(verbose_name='cuit_chofer')
    patente_camion = models.CharField(max_length=20, verbose_name='patente_chasis')
    patente_acoplado = models.CharField(max_length=20, verbose_name='patente_acomplado')
    fecha_actual = models.DateField(verbose_name='fecha_actual')

    class Meta: 
        db_table = 'balanza'

    def __str__(self): 
        return '%s, %s %s' % (self.patente_camion, self.patente_acoplado)
    """
    NO SE REALIZO NINGUN MAKEMIGRATIONS AUN - NI TAMPOCO UN MIGARTE DE ESTA TABLA.
    """