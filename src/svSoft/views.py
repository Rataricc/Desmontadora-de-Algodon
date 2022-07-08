from django.shortcuts import render

def index(request):
    template_name = "base/index.html"
    ctx = {}
    return render(request, template_name, ctx)