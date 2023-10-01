#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppFamiliares.models import Familiar

# Create your views here.
def listar_familiares(request):
    context = { "misFamiliares": Familiar.objects.all() }
    plantilla = loader.get_template("familiares_v1.html")

    # for i in Familiar.objects.all():
    #     print(i.name)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(context)

    return HttpResponse(documento)
