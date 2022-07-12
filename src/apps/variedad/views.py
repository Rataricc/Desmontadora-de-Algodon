from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from apps.variedad .forms           import VariedadForm 
from django.views.generic           import ListView
from django.shortcuts               import render
from .models                        import Variedad
from django.urls                    import reverse_lazy
from django.views.generic.edit      import UpdateView

# Create your views here.

@login_required
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

class TablaVariedad(LoginRequiredMixin, ListView): 
    template_name = 'variedad/tabla_variedad.html'
    model = Variedad
    context_object_name = 'variedad'

class EditarTablaVariedad(UpdateView): 
    template_name = 'variedad/editar_tabla_variedad_semilla.html'
    model = Variedad
    form_class = VariedadForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('variedad:tablavariedad')
