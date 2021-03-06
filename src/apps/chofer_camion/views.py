from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts               import render
from django.views.generic           import ListView
from .models                        import Chofer, Camion
from apps.chofer_camion .forms      import ChoferForm, CamionForm
from django.urls                    import reverse_lazy
from django.views.generic.edit      import UpdateView
from django.views.generic 			import DeleteView
from django.db.models               import Q

# Create your views here.

@login_required
def chofer(request): 
    template_name = "chofer/chofer.html"
    form=ChoferForm()
    if request.method == 'POST': 
        form = ChoferForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaChofer(LoginRequiredMixin, ListView): 
    template_name = 'chofer/tabla_chofer.html'
    model = Chofer
    context_object_name = 'chofer'

    def get_queryset(self):
        queryset = self.request.GET.get("buscar")
        clientes =  Chofer.objects.all()
        if queryset: 
            cliente = Chofer.objects.filter(
                Q(codigo_transportista__icontains = queryset) |
                Q(descripcion_transportista__icontains = queryset)
            ).distinct() 
            
            return cliente
        return clientes

@login_required
def camion(request): 
    template_name = "camion/camion.html"
    form=CamionForm()
    if request.method == 'POST': 
        form = CamionForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaCamion(LoginRequiredMixin, ListView): 
    template_name = 'camion/tabla_camion.html'
    model = Camion
    context_object_name = 'camion'

    def get_queryset(self):
        queryset = self.request.GET.get("buscar")
        clientes =  Camion.objects.all()
        if queryset: 
            cliente = Camion.objects.filter(
                Q(id__icontains = queryset) |
                Q(patente_camion__icontains = queryset) |
                Q(patente_acomplado__icontains = queryset)
            ).distinct() 
            
            return cliente
        return clientes


class EditarTablaChofer(LoginRequiredMixin, UpdateView): 
    template_name = 'chofer/editar_tabla_chofer.html'
    model = Chofer
    form_class = ChoferForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('chofer_camion:tablachofer')

class EditarTablaCamion(LoginRequiredMixin, UpdateView): 
    template_name = 'camion/editar_tabla_camion.html'
    model = Camion
    form_class = CamionForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('chofer_camion:tablacamion')

class EliminarCampoChofer(LoginRequiredMixin, DeleteView):
	model = Chofer
	template_name = 'chofer/eliminar_chofer.html' 

	def get_success_url(self, **kwargs): 
		return reverse_lazy('chofer_camion:tablachofer')

class EliminarCampoCamion(LoginRequiredMixin, DeleteView):
	model = Camion
	template_name = 'camion/eliminar_camion.html' 

	def get_success_url(self, **kwargs): 
		return reverse_lazy('chofer_camion:tablacamion')