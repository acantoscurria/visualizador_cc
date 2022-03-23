from curses.ascii import HT
import json
from django.shortcuts import render, HttpResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse
import pdb

from numpy import VisibleDeprecationWarning
from . models import TablaLocalizaciones,VistaPadronOfertas


# Create your views here.
def inicio(request):
      return render(request,'inicio/index.html',{})

def nuevo_mapa(request):
      capa_unica = serialize('geojson', TablaLocalizaciones.objects.all(),
      geometry_field='geom',
      fields=('id','cueanexo',))
      # departamento = TablaLocalizaciones.objects.values_list("departamento",flat=True).distinct("departamento")
      # loc = TablaLocalizaciones.objects.values_list("localidad",flat=True).distinct("localidad")
      return render(request, 'nuevo_mapa.html', {'establecimientos': capa_unica,})
      # return HttpResponse(capa_unica) 


def datosPadron(request,cueanexo = ''):
      if cueanexo:
            datos = VistaPadronOfertas.objects.filter(cueanexo = cueanexo)
            
      else: 
            datos = VistaPadronOfertas.objects.all()

      datos = serialize('json', datos)
      return HttpResponse(datos, content_type='application/json')


