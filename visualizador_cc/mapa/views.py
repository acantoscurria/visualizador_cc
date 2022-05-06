
from django.shortcuts import render, HttpResponse
from visualizador_cc.mapa.serializers.MapaSerializer import TablaLocalizacionesSerializer,PadronOfertaSerializer, TablaLocalizacionesSearchSerializer
from . models import TablaLocalizaciones,Padron
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from django.db.models import Q
from django.views.generic.list import ListView
from django.http import JsonResponse


class Mapa(TemplateView):
    template_name = 'mapa/index.html' 
    http_method_names = ['get'] 
    extra_context = {
        'title': 'Mapa'
    }
 
    
class Points(generics.ListAPIView):
  
    serializer_class = TablaLocalizacionesSerializer
    permission_class= AllowAny
    queryset = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo')
             

class PointData(generics.ListAPIView):

    serializer_class = PadronOfertaSerializer
    permission_class= AllowAny

    def get_queryset(self):

        cueanexo = self.request.query_params.get('cueanexo')
        print('PointData cueanexo', cueanexo)
        if cueanexo:
            return Padron.objects.all().filter(cueanexo=cueanexo)
        else:
            return []




class Search(ListView):

    def post(self, request, *args, **kwargs):

        dt = request.POST
        draw = int(dt.get("draw"))
        start = int(dt.get("start"))
        length = int(dt.get("length"))

        print('start', start)
        print('length', length)

        recordsTotal = 0
        data = []
        recordsFiltered = 0

        search = dt.get("search[value]")

        print('search', search)     
      
        recordsTotal = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').count()

        if search: # si hay valor de busqueda

            # obtengo todas las filas filtradas sin paginacion
            object_list = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').filter(
                Q(cueanexo__nom_est__icontains=search)
            )

            # obtengo la cantidad de filas filtrdas sin paginacion
            recordsFiltered = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').filter(
                Q(cueanexo__nom_est__icontains=search)
            ).count()

        else: # no hay valor de busqueda

            return JsonResponse({
                "draw": draw,
                "recordsTotal": recordsTotal,
                "recordsFiltered": recordsFiltered,
                "data": []               
            }, 
            safe=False)


        # data = []  
        # for row in object_list:
        #     # print('parse', row.parse())
        #     data.append(row.parse())
       
    
        return JsonResponse({
            "draw": draw,
            "recordsTotal": recordsTotal,
            "recordsFiltered": recordsFiltered,
            "data": object_list         
        }, 
        safe=False)