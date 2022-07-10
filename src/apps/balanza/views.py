from django.views.generic   import ListView
from .models                import Balanza
from django.shortcuts       import render
from apps.balanza .forms    import BalanzaForm 
# Create your views here.

def balanza(request): 
    template_name = "balanza/balanza.html"
    form=BalanzaForm()
    if request.method == 'POST': 
        form = BalanzaForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaBalanza(ListView): 
    template_name = 'balanza/tabla_balanza.html'
    model = Balanza
    context_object_name = 'balanza'