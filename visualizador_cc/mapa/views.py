from curses.ascii import HT
import json
from django.shortcuts import render, HttpResponse
from django.core.serializers import serialize
import pdb
from . models import TablaLocalizaciones,Padron,PadronOferta


# Create your views here.
def inicio(request):
      return render(request,'inicio/index.html',{})

def nuevo_mapa(request):
      capa_unica = serialize('geojson', [*TablaLocalizaciones.objects.all(),*Padron.objects.all()],
      geometry_field='geom')
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


