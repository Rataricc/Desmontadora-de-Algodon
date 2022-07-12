from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic           import ListView
from django.shortcuts               import render
from .forms                         import PadronForm
from .models                        import Padron
# Create your views here.

@login_required
def padron(request): 
    template_name = "padron/padron.html"
    form=PadronForm()
    if request.method == 'POST': 
        form = PadronForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaPadron(LoginRequiredMixin, ListView): 
    template_name = 'padron/tabla_padron.html'
    model = Padron
    context_object_name = 'padron'