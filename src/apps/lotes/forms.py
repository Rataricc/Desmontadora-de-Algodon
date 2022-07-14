from django                      import forms
from apps.establecimiento.models import Establecimiento
from apps.padron.models          import Padron
from .models                     import Lotes

class LotesForm(forms.ModelForm): 
    padron = forms.ModelChoiceField(queryset=Padron.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    establecimiento = forms.ModelChoiceField(queryset=Establecimiento.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Lotes
        fields = ["padron", "establecimiento"]