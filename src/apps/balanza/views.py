from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic           import ListView
from django.views.generic.edit      import UpdateView
from .models                        import Balanza
from django.shortcuts               import render
from apps.balanza .forms            import BalanzaForm 
from django.urls                    import reverse_lazy
from django.views.generic 			import DeleteView

# Create your views here.

@login_required
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

class TablaBalanza(LoginRequiredMixin, ListView): 
    template_name = 'balanza/tabla_balanza.html'
    model = Balanza
    context_object_name = 'balanza'

class EditarTabla(LoginRequiredMixin, UpdateView): 
    template_name = 'balanza/editar_tabla.html'
    model = Balanza
    form_class = BalanzaForm 

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('balanza:tablabalanza')

class EliminarCampoBalanza(LoginRequiredMixin, DeleteView):
	model = Balanza
	template_name = 'balanza/eliminar_balanza.html' 

	def get_success_url(self, **kwargs): 
		return reverse_lazy('balanza:tablabalanza')