from django     import forms
from .models    import Balanza

class BalanzaForm(forms.ModelForm): 
    class Meta:
        model = Balanza
        fields = ["padron", "codigo_productor", "tipo_alg", "establecimiento", "lotes", "variedad", "chofer", "cuit_chofer", "patente_camion", 
        "patente_acoplado", "fecha_actual"]