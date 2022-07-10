from apps.variedad .forms   import VariedadForm 
from django.views.generic   import ListView
from django.shortcuts       import render
from .models                import Variedad
# Create your views here.


def variedad(request): 
    template_name = "variedad/variedad.html"
    form=VariedadForm()
    if request.method == 'POST': 
        form = VariedadForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaVariedad(ListView): 
    template_name = 'variedad/tabla_variedad.html'
    model = Variedad
    context_object_name = 'variedad'
