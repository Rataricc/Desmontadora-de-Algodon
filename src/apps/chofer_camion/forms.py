from django import forms
from .models import Chofer,Camion

class ChoferForm(forms.ModelForm): 
    class Meta:
        model = Chofer
        fields = ["descripcion_transportista", "carnet_conducir_chofer", "num_cuit_chofer", "padron"]


class CamionForm(forms.ModelForm): 
    class Meta:
        model = Camion
        fields = ["chofer", "patente_camion", "patente_acomplado"]