from django import forms
from .models import Padron

class PadronForm(forms.ModelForm): 
    nombre_completoApellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Padron
        fields = ["nombre_completoApellidos"]