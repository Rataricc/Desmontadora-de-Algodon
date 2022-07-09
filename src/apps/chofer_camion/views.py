from django.shortcuts          import render
from django.views.generic      import ListView
from .models                   import Chofer, Camion
from apps.chofer_camion .forms import ChoferForm, CamionForm
# Create your views here.


def chofer(request): 
    template_name = "chofer/chofer.html"
    form=ChoferForm()
    if request.method == 'POST': 
        form = ChoferForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaChofer(ListView): 
    template_name = 'chofer/tabla_chofer.html'
    model = Chofer
    context_object_name = 'chofer'

def camion(request): 
    template_name = "camion/camion.html"
    form=CamionForm()
    if request.method == 'POST': 
        form = CamionForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaCamion(ListView): 
    template_name = 'camion/tabla_camion.html'
    model = Camion
    context_object_name = 'camion'