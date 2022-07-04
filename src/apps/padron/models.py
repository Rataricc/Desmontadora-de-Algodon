from django.db import models

# Create your models here.

class Padron(models.Model):
    codigo_cliente = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    nombre_completoApellidos = models.CharField(max_length=50)
    
    class Meta: 
        db_table = 'padron'

    def __str__(self):
        return self.nombre_completoApellidos

class Establecimiento(models.Model): 
    padron = models.ForeignKey(Padron, on_delete=models.CASCADE)
    codigo_establecimiento = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    descripcion_establecimiento = models.CharField(max_length=30)
    provincia = models.CharField(max_length=20)
    departamento = models.CharField(max_length=20)

    class Meta: 
        db_table = 'establecimiento'

    def __str__(self): 
        return self.descripcion_establecimiento + '' + self. provincia + '' + self.departamento

class Lotes(models.Model): 
    padron = models.ForeignKey(Padron, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    numero_lote = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID') 

    class Meta: 
        db_table = 'lotes'

    