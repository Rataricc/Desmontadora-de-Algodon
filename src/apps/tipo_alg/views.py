from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic           import ListView
from django.shortcuts               import render
from apps.tipo_alg .forms           import Tipo_AlgForm 
from .models                        import Tipo_Alg
from django.urls                    import reverse_lazy
from django.views.generic.edit      import UpdateView
from django.views.generic 			import DeleteView

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

class EditarTablaTipoAlgodon(LoginRequiredMixin, UpdateView): 
    template_name = 'tipo_alg/editar_tabla_tipo_algodon.html'
    model = Tipo_Alg
    form_class = Tipo_AlgForm 

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('tipo_alg:tablatipoalgodon')

class EliminarCampoTipo_alg(LoginRequiredMixin, DeleteView):
	model = Tipo_Alg
	template_name = 'tipo_alg/eliminar_tipo_alg.html' 

	def get_success_url(self, **kwargs): 
		return reverse_lazy('tipo_alg:tablatipoalgodon')