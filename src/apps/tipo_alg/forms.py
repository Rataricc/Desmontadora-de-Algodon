from django     import forms
from .models    import Tipo_Alg

class Tipo_AlgForm(forms.ModelForm): 
    class Meta:
        model = Tipo_Alg
        fields = ["descripcion_cosecha"]