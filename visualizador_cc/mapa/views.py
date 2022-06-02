
from re import L
from django.shortcuts import render, HttpResponse
from visualizador_cc.mapa.serializers.MapaSerializer import TablaLocalizacionesSerializer
from . models import TablaLocalizaciones, Padron
from visualizador_cc.mapa.serializers.MapaSerializer import TablaLocalizacionesSerializer,PadronSerializer
from . models import TablaLocalizaciones,Padron
from .serializers import *
from rest_framework import generics,views,status
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.gis.geos import Point
from django.views.generic.list import ListView
from django.http import JsonResponse
import json

class MapaGeneral(TemplateView):
    template_name = 'pages/mapa_general.html'
    http_method_names = ['get']
    extra_context = {
        'title': 'Mapa General'
    }

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


class Filter(ListView):

    def post(self, request, *args, **kwargs):   

        filter = json.loads(request.POST.get('filter'))

        sector = filter['sector']
        ambito = filter['ambito']
        departamento = filter['departamento']

        print('Filter.post sector', sector)
        print('Filter.post ambito', ambito)
        print('Filter.post departamento', departamento)

        object_list = Padron.objects.all().filter(estado_loc='Activo')

        empty = True

        if(len(sector) > 0):
            # print('Filter hay sector', len(sector))
            object_list = object_list.filter(sector__in=sector)
            empty = False

        if(len(ambito) > 0):
            # print('Filter hay ambito', len(ambito))
            object_list = object_list.filter(ambito__in=ambito)
            empty = False

        if(len(departamento) > 0):
            # print('Filter hay departamento', len(departamento))
            object_list = object_list.filter(departamento__in=departamento)
            empty = False

        print('Filter empty', empty)

        if(empty): 
            return JsonResponse([], safe=False)    

        data = []  
        for row in object_list:  
            data.append(row.cueanexo)         

        print('Filter data', len(data))

        return JsonResponse(data, safe=False)        

class PointData(generics.ListAPIView):

    serializer_class = PadronSerializer
    permission_class= AllowAny

    def get_queryset(self):

        cueanexo = self.request.query_params.get('cueanexo')
        print('PointData cueanexo', cueanexo)
        if cueanexo:
            return Padron.objects.all().filter(cueanexo=cueanexo)
        else:
            return []




class LocalizacionesByCircle(TemplateView):

    template_name = 'mapa/localizaciones.html'
    http_method_names = ['get']    

    def get(self, request, *args, **kwargs):   
        context = self.get_context_data(**kwargs)        
        context['radio'] = request.GET.get('radio')
        context['centro'] = request.GET.get('coordenadas')
        context['title'] = 'Localizaciones seleccionadas'
        
        return self.render_to_response(context)   

class LocalizacionesByCircleList(ListView):

    def post(self, request, *args, **kwargs): 

        dt = request.POST      
        radio = dt.get("radio")    
        centro = dt.get("centro") 
   
        if(radio == '' or centro == ''):            
            return JsonResponse({"data": []}, safe=False)  

        centro = centro.split(',')

        buffer = Point(float(centro[0]), float(centro[1]), srid=4326).buffer(float(radio)/100000)

        data = [] 
        for loc in  TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo'):     
            if buffer.contains(loc.geom):
                print('### LocalizacionesByCircleList...', loc.cueanexo.cueanexo)
                data.append(loc.parse())

        return JsonResponse({                    
            "data": data                
        }, 
        safe=False)



class Search(ListView):

    def post(self, request, *args, **kwargs):

        dt = request.POST
        draw = int(dt.get("draw"))
        start = int(dt.get("start"))
        length = int(dt.get("length"))
        search = dt.get("search[value]")

      
        print('start', start)
        print('length', length)     
        print('search', search)   

        cueanexo_value_int = 0
        if(search.isnumeric()):
            cueanexo_value_int = int(search)

        recordsTotal = 0
        data = []
        recordsFiltered = 0
                
       
        recordsTotal = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').count()

        if search: # si hay valor de busqueda

            if(length != -1): #hay paginacion

                # obtengo todas las filas filtradas con paginacion
                object_list = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').filter(
                    Q(cueanexo__nom_est__icontains=search) | Q(cueanexo=cueanexo_value_int) 
                )[start:start+length]

            else:

                # obtengo todas las filas filtradas sin paginacion
                object_list = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').filter(
                    Q(cueanexo__nom_est__icontains=search) | Q(cueanexo=cueanexo_value_int) 
                )

            # obtengo la cantidad de filas filtrdas sin paginacion
            recordsFiltered = TablaLocalizaciones.objects.all().filter(cueanexo__estado_loc='Activo').filter(
                Q(cueanexo__nom_est__icontains=search) | Q(cueanexo=cueanexo_value_int) 
            ).count()

        else: # no hay valor de busqueda

            return JsonResponse({
                "draw": draw,
                "recordsTotal": recordsTotal,
                "recordsFiltered": recordsFiltered,
                "data": []               
            }, 
            safe=False)

        i = 0

        data = []  
        for row in object_list:       
            data.append(row.parse())
            i = i + 1

        print('i', i)
        print('len', len(data))

        return JsonResponse({
            "draw": draw,
            "recordsTotal": recordsTotal,
            "recordsFiltered": recordsFiltered,
            "data": data         
        }, 
        safe=False)
