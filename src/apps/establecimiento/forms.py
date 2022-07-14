from msilib.schema import Font
from django import forms

from apps.padron.models import Padron
from .models import Establecimiento

class EstablecimientoForm(forms.ModelForm): 
    padron = forms.ModelChoiceField(queryset=Padron.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    descripcion_establecimiento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    provincia =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    departamento = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Establecimiento
        fields = ["padron", "descripcion_establecimiento", "provincia", "departamento"]