from urllib import request
from apps.establecimiento.models import Establecimiento
from apps.lotes.models           import Lotes
from apps.padron.models          import Padron
from apps.tipo_alg.models        import Tipo_Alg
from apps.variedad.models        import Variedad
from apps.chofer_camion.models   import Chofer
from django                      import forms
from .models                     import Balanza
from django.db.models            import Q

class BalanzaForm(forms.ModelForm): 
    padron = forms.ModelChoiceField(queryset=Padron.objects.filter(), empty_label="(Seleccione un articulo)", widget=forms.Select(attrs={'class':'form-control'}))
    codigo_productor = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    tipo_alg = forms.ModelChoiceField(queryset=Tipo_Alg.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    establecimiento = forms.ModelChoiceField(queryset=Establecimiento.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    lotes = forms.ModelChoiceField(queryset=Lotes.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    variedad = forms.ModelChoiceField(queryset=Variedad.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    chofer = forms.ModelChoiceField(queryset=Chofer.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    cuit_chofer = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    patente_camion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    patente_acoplado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    fecha_actual = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))

    class Meta:
        model = Balanza
        fields = ["padron", "codigo_productor", "tipo_alg", "establecimiento", "lotes", "variedad", "chofer", "cuit_chofer", "patente_camion", 
        "patente_acoplado", "fecha_actual"]