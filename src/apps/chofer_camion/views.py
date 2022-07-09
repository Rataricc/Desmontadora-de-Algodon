from django.shortcuts          import render
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