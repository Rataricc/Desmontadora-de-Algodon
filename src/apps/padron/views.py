from django.shortcuts import render
from .forms import PadronForm
# Create your views here.

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