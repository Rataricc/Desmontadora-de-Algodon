from django.shortcuts               import render
from apps.balanza .models           import Balanza
from apps.padron .models            import Padron 
from django.contrib.auth.decorators import login_required


def index(request):
    template_name = "base/index.html"
    ctx = {}
    return render(request, template_name, ctx)

@login_required
def mostrarDatos(request): 
    template_name = "base/mostrar.html"
    lista_balaza = Balanza.objects.all()
    lista_padron = Padron.objects.all()
    ctx = {
        'lista_balaza': lista_balaza,
        'lista_padron': lista_padron
    }
    return render(request, template_name, ctx)
