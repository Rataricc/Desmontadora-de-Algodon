from django.shortcuts    import render
from apps.tipo_alg .forms import Tipo_AlgForm 
# Create your views here.


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