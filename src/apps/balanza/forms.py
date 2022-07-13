from django     import forms

from apps.padron.models import Padron
#queryset=Padron.objects.all(),
from .models    import Balanza

class BalanzaForm(forms.ModelForm): 
    padron = forms.ModelChoiceField(queryset=Padron.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    class Meta:
        model = Balanza
        fields = ["padron", "codigo_productor", "tipo_alg", "establecimiento", "lotes", "variedad", "chofer", "cuit_chofer", "patente_camion", 
        "patente_acoplado", "fecha_actual"]