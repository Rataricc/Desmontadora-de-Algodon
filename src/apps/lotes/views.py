from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic           import ListView
from django.shortcuts               import render
from .models                        import Lotes
from .forms                         import LotesForm


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