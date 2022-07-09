from django.shortcuts    import render
from apps.balanza .forms import BalanzaForm 
# Create your views here.

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