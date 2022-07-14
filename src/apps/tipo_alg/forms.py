from django     import forms
from .models    import Tipo_Alg

class Tipo_AlgForm(forms.ModelForm): 
    descripcion_cosecha = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Tipo_Alg
        fields = ["descripcion_cosecha"]