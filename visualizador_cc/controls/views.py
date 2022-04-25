
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from visualizador_cc.users.models import User
from django.views.generic.list import ListView

from visualizador_cc.controls.models import (
    ConMatricComunInicial,
    ConMatricComunSecundaria
)
# Create your views here.


class ControlsMatriculaIndexView(View):
    def get(self, request):
        context = {"title": "Control de Mátriculas - RA 2022"}
        return render(request, "controls/matricula.html", context)


class ControlsMatriculaListView(ListView):

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
        object_list = None

        search = dt.get("search[value]")
        matricula_selected = dt.get("matricula_selected")    
        control_type_selected = dt.get("control_type_selected")     

        print('matricula_selected', matricula_selected)
        print('control_type_selected', control_type_selected)

        if(matricula_selected == "none" or control_type_selected == "none"):            
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": recordsTotal,
                        "recordsFiltered": recordsFiltered,
                        "data": data,
                        "error_msg": "",
                    }, 
                    safe=False)    


        if(matricula_selected == "matricula_comun_inicial"):

            recordsTotal = ConMatricComunInicial.objects.all().count()

            recordsFiltered  = recordsTotal

            if(length != -1): #hay paginacion
                page_number = start / length + 1     

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = ConMatricComunInicial.objects.filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[page_number:length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = ConMatricComunInicial.objects.filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = ConMatricComunInicial.objects.filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = ConMatricComunInicial.objects.all()[page_number:length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = ConMatricComunInicial.objects.all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = ConMatricComunInicial.objects.filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        elif(matricula_selected == "matricula_comun_secundaria"):

            recordsTotal = ConMatricComunSecundaria.objects.all().count()

            recordsFiltered  = recordsTotal

            if(length != -1): #hay paginacion
                page_number = start / length + 1     

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = ConMatricComunSecundaria.objects.filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[page_number:length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = ConMatricComunSecundaria.objects.filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = ConMatricComunSecundaria.objects.filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = ConMatricComunSecundaria.objects.all()[page_number:length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = ConMatricComunSecundaria.objects.all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = ConMatricComunSecundaria.objects.filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        data = []  
        for row in object_list:
            # print('parse', row.parse())
            data.append(row.parse())
        
       
        # print('data', data)

        return JsonResponse({
            "draw": draw,
            "recordsTotal": recordsTotal,
            "recordsFiltered": recordsFiltered,
            "data": data,
            "error_msg": "",
        }, 
        safe=False)


