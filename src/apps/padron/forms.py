from django import forms
from .models import Padron

class PadronForm(forms.ModelForm): 
    class Meta:
        model = Padron
        fields = ["nombre_completoApellidos"]