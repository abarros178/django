from django.http import HttpResponse
import datetime
from django.template import Template,Context

def saludo(request):
    doc_externo=open("C:/Users/abarros17/Desktop/django/proyecto1/proyecto1/plantillas/misplantillas.html")
    plt=Template(doc_externo.read())
    doc_externo.close
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego")

def damefecha(request):
    fechaactual=datetime.datetime.now()
    documento="""
    <html>
    <body>
    <h2>
    Fecha y hora actuales son: %s
    <h2>
    </body>
    </html>
    """ % fechaactual
    return HttpResponse(documento)

def calcularEdad(request,edad,agno):
    edadactual=edad
    periodo=agno-2022
    edadFutura=edadactual+periodo
    documento="""
    <html>
    <body>
    <h2>
    En el año %s tendras %s años
    <h2>
    </body>
    </html>
    """ %(agno,edadFutura)

    return HttpResponse(documento)


