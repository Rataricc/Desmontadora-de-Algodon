from django.shortcuts           import render
from apps.establecimiento.forms import EstablecimientoForm

# Create your views here.

def establecimiento(request): 
    template_name = "establecimiento/establecimiento.html"
    form=EstablecimientoForm()
    if request.method == 'POST': 
        form = EstablecimientoForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)