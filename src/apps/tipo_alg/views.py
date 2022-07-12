from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic           import ListView
from django.shortcuts               import render
from apps.tipo_alg .forms           import Tipo_AlgForm 
from .models                        import Tipo_Alg
# Create your views here.

@login_required
def tipo_alg(request): 
    template_name = "tipo_alg/tipo_alg.html"
    form=Tipo_AlgForm()
    if request.method == 'POST': 
        form = Tipo_AlgForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaTipoAlgodon(LoginRequiredMixin, ListView): 
    template_name = 'tipo_alg/tabla_tipo_alg.html'
    model = Tipo_Alg
    context_object_name = 'algodon'