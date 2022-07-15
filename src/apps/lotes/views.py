from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic           import ListView
from django.shortcuts               import render
from .models                        import Lotes
from .forms                         import LotesForm
from django.urls                    import reverse_lazy
from django.views.generic.edit      import UpdateView
from django.views.generic 			import DeleteView


# Create your views here.

@login_required
def lotes(request): 
    template_name = "lotes/lotes.html"
    form=LotesForm()
    if request.method == 'POST': 
        form = LotesForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)

class TablaLotes(LoginRequiredMixin, ListView): 
    template_name = 'lotes/tabla_lotes.html'
    model = Lotes
    context_object_name = 'lotes'

class EditarTablaLotes(LoginRequiredMixin, UpdateView): 
    template_name = 'lotes/editar_tabla_lotes.html'
    model = Lotes
    form_class = LotesForm

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('lotes:tablalotes')

class EliminarCampoLotes(LoginRequiredMixin, DeleteView):
	model = Lotes
	template_name = 'lotes/eliminar_lotes.html' 

	def get_success_url(self, **kwargs): 
		return reverse_lazy('lotes:tablalotes')