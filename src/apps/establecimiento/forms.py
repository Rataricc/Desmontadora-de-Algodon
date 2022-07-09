from django import forms
from .models import Establecimiento

class EstablecimientoForm(forms.ModelForm): 
    class Meta:
        model = Establecimiento
        fields = ["padron", "descripcion_establecimiento", "provincia", "departamento"]