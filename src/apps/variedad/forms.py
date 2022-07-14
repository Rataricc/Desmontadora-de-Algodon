from django     import forms
from .models    import Variedad

class VariedadForm(forms.ModelForm): 
    descripcion_variedad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Variedad
        fields = ["descripcion_variedad"]