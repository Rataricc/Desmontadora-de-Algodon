from django.db                   import models
from apps.establecimiento.models import Establecimiento
from apps.chofer_camion.models   import Chofer
from apps.tipo_alg.models        import Tipo_Alg
from apps.variedad.models        import Variedad
from apps.padron.models          import Padron
from apps.lotes.models           import Lotes


# Create your models here.

class Balanza(models.Model): 
    numero_remito = models.BigAutoField(primary_key=True, unique=True, editable=False, verbose_name='ID') 
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
        return self.patente_camion + '' + self.patente_acoplado
"""
    def save(self, *args, **kwargs): 
        if self.numero_remito is None: 
            last_numero_remito = self.__class__.objects.all().order_by('numero_remito').last()
            if last_numero_remito is None: 
                last_numero_remito = '000000000000'
            last_numero_remito_number = ''.join(substr for substr in last_numero_remito if substr.isdigit())
            leading_zeros = len(last_numero_remito_number) - 1
            incremented_number = int(last_numero_remito_number) + 1
            incremented_number = str(incremented_number).zfill(leading_zeros)
            self.numero_remito = f'{incremented_number}'
        super(Balanza, self).save(*args, **kwargs)
"""

#balanza1 = Balanza('00000000001', '4', '2', '1', '1', '1', '1', '4', '1234567', '1hf2345', 'h3435gd', '2022-07-07')
#balanza1.save()

