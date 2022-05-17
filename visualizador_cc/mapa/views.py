
from django.shortcuts import render, HttpResponse
from visualizador_cc.mapa.serializers.MapaSerializer import TablaLocalizacionesSerializer, PadronOfertaSerializer, TablaLocalizacionesSearchSerializer
from . models import TablaLocalizaciones, Padron
from .serializers import *
from rest_framework import generics,views,status
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.gis.geos import Point

# Create your views here.

# def nuevo_mapa(request):
#       capa_unica = serialize('geojson', [*TablaLocalizaciones.objects.all(),*Padron.objects.all()],
#       geometry_field='geom',use_natural_foreign_keys=True, use_natural_primary_keys=True)
#       capa_unica = serialize('geojson', TablaLocalizaciones.objects.all(),
#       geometry_field='geom')

#       return HttpResponse(capa_unica.data)


class Mapa(TemplateView):
    template_name = 'mapa/index.html'
    http_method_names = ['get']
    extra_context = {
        'title': 'Mapa'
    }


class Points(generics.ListAPIView):

    serializer_class = TablaLocalizacionesSerializer
    permission_class = AllowAny
    queryset = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo')


class Search(generics.ListAPIView):

    serializer_class = TablaLocalizacionesSearchSerializer
    permission_class = AllowAny

    def get_queryset(self):

        q = self.request.query_params.get('q')
        print('Points q', q)

        # q = 6545646, pepe

        if q:
            # return TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo' | cueanexo__nom_est_ilike=)

            return TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').filter(
                Q(nom_est__icontains=q) | Q(cueanexo__icontains=q)
            )[:5]

        else:
            return []


class PointData(generics.ListAPIView):

    serializer_class = PadronOfertaSerializer
    permission_class = AllowAny

    def get_queryset(self):

        cueanexo = self.request.query_params.get('cueanexo')
        print('PointData cueanexo', cueanexo)
        if cueanexo:
            return Padron.objects.all().filter(cueanexo=cueanexo)
        else:
            return []


class SpatialQuery(generics.GenericAPIView):

    http_method_names = ['post']
    permission_classes = [AllowAny]  

    def post(self,request):
        rad = request.data.get('radio')
        centro = request.data.get('coordenadas')
        print(rad)
        print(centro)

        buffer = Point(centro,srid=4326).buffer(rad/100000)

        for loc in TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo'):
            if buffer.contains(loc.geom):
                print(loc.cueanexo)

        return Response({},
        status=status.HTTP_200_OK)

