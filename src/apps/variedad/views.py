from django.shortcuts    import render
from apps.variedad .forms import VariedadForm 
# Create your views here.


def variedad(request): 
    template_name = "variedad/variedad.html"
    form=VariedadForm()
    if request.method == 'POST': 
        form = VariedadForm(request.POST)
        if form.is_valid(): 
            form.save()
    ctx = {
        'form':form
    }
    return render(request, template_name, ctx)
# Create your views here.
