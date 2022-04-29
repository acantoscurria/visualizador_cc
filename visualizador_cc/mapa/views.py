from django.shortcuts import render, HttpResponse
from visualizador_cc.mapa.serializers.MapaSerializer import TablaLocalizacionesSerializer,PadronOfertaSerializer
from . models import TablaLocalizaciones,Padron
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView

# Create your views here.

# def nuevo_mapa(request):
#       capa_unica = serialize('geojson', [*TablaLocalizaciones.objects.all(),*Padron.objects.all()],
#       geometry_field='geom',use_natural_foreign_keys=True, use_natural_primary_keys=True)
#       capa_unica = serialize('geojson', TablaLocalizaciones.objects.all(), 
#       geometry_field='geom')

#       return HttpResponse(capa_unica.data)


class Visualizador(TemplateView):
    template_name = 'mapa/nuevo-mapa.html' 
    http_method_names = ['get'] 
    
class MapaList(generics.ListAPIView):

    queryset = TablaLocalizaciones.objects.all()
    serializer_class = TablaLocalizacionesSerializer
    permission_class= AllowAny


class DatosMapaList(generics.ListAPIView):

    serializer_class = PadronOfertaSerializer
    permission_class= AllowAny

    def get_queryset(self):

        queryset = Padron.objects.all()
        cueanexo = self.request.query_params.get('cueanexo')
        if cueanexo is not None:
            queryset = queryset.filter(cueanexo=cueanexo)
        return queryset
