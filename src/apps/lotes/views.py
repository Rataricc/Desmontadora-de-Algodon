from django.shortcuts import render
from .forms import LotesForm


# Create your views here.

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