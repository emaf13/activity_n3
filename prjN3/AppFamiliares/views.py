#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def listar_familiares(request, familiar):
    plantilla = loader.get_template("familiares_v1.html")

    # for i in Familiar.objects.all():
    #     print(i.name)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(familiar)

    return HttpResponse(documento)
