from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from apps.establecimiento.forms     import EstablecimientoForm
from .models                        import Establecimiento
from django.shortcuts               import render
from django.views.generic           import ListView
from django.urls                    import reverse_lazy
from django.views.generic.edit      import UpdateView
from django.views.generic 			import DeleteView

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

class EditarTablaEstablecimiento(LoginRequiredMixin, UpdateView): 
    template_name = 'establecimiento/editar_tabla_establecimiento.html'
    model = Establecimiento
    form_class = EstablecimientoForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('establecimineto:tablaestablecimiento')

class EliminarCampoEstablecimiento(LoginRequiredMixin, DeleteView):
	model = Establecimiento
	template_name = 'establecimiento/eliminar_establecimiento.html' 

	def get_success_url(self, **kwargs): 
		return reverse_lazy('establecimineto:tablaestablecimiento')