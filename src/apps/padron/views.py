from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic           import ListView
from django.shortcuts               import render
from .forms                         import PadronForm
from .models                        import Padron
from django.urls                    import reverse_lazy
from django.views.generic.edit      import UpdateView
from django.views.generic 			import DeleteView

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

class EditarTablaPadron(LoginRequiredMixin, UpdateView): 
    template_name = 'padron/editar_tabla_padron.html'
    model = Padron
    form_class = PadronForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('padron:tablapadron')

class EliminarCampoPadron(LoginRequiredMixin, DeleteView):
	model = Padron
	template_name = 'padron/eliminar_padron.html' 

	def get_success_url(self, **kwargs): 
		return reverse_lazy('padron:tablapadron')