from django import forms
from .models import Lotes

class LotesForm(forms.ModelForm): 
    class Meta:
        model = Lotes
        fields = ["padron", "establecimiento"]