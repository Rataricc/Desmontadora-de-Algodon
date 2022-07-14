from django     import forms
from .models    import Tipo_Alg

VARIEDAD_COSECHA = (
    ("MANUAL", "MANUAL"), 
    ("STRIPER", "STRIPER"), 
    ("USILLO", "USILLO")
)

class Tipo_AlgForm(forms.ModelForm): 
    descripcion_cosecha = forms.CharField(widget=forms.Select(choices=VARIEDAD_COSECHA, attrs={'class':'form-control'}))
    
    class Meta:
        model = Tipo_Alg
        fields = ["descripcion_cosecha"]