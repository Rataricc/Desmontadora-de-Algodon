from apps.padron.models import Padron
from .models import Chofer,Camion
from django import forms

class ChoferForm(forms.ModelForm): 
    descripcion_transportista = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    carnet_conducir_chofer = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    num_cuit_chofer = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    padron = forms.ModelChoiceField(queryset=Padron.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Chofer
        fields = ["descripcion_transportista", "carnet_conducir_chofer", "num_cuit_chofer", "padron"]


class CamionForm(forms.ModelForm): 
    chofer = forms.ModelChoiceField(queryset=Chofer.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    patente_camion = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    patente_acomplado = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Camion
        fields = ["chofer", "patente_camion", "patente_acomplado"]