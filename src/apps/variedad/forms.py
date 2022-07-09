from django     import forms
from .models    import Variedad

class VariedadForm(forms.ModelForm): 
    class Meta:
        model = Variedad
        fields = ["descripcion_variedad"]