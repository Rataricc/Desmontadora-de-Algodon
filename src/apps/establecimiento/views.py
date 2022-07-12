from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from apps.establecimiento.forms     import EstablecimientoForm
from .models                        import Establecimiento
from django.shortcuts               import render
from django.views.generic           import ListView

# Create your views here.

@login_required
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

class TablaEstablecimiento(LoginRequiredMixin, ListView): 
    template_name = 'establecimiento/tabla_establecimiento.html'
    model = Establecimiento
    context_object_name = 'establecimiento'