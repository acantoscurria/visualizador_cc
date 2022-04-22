
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from visualizador_cc.users.models import User
from django.views.generic.list import ListView

from visualizador_cc.controls.models import (
    ConMatricComunInicial,
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

        search = dt.get("search[value]")
        matricula_selected = dt.get("matricula_selected")    
        control_type_selected = dt.get("control_type_selected")     

        print('matricula_selected', matricula_selected)
        print('control_type_selected', control_type_selected)

        if(matricula_selected == "none" or control_type_selected == "none"):            
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": 0,
                        "recordsFiltered": [],
                        "data": [],
                        "error_msg": "",
                    }, 
                    safe=False)

        

        total = ConMatricComunInicial.objects.all().count()
        filtered = total
        matriculasComunInicial = ConMatricComunInicial.objects.all()

        if search:
            matriculasComunInicial = ConMatricComunInicial.objects.filter(
                Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
            )
            total = matriculasComunInicial.count()
            filtered = total

        # paginator
        paginator = Paginator(matriculasComunInicial, length)

        page_number = start / length + 1

        try:
            object_list = paginator.page(page_number).object_list
        except PageNotAnInteger:
            object_list = paginator.page(1).object_list
        except EmptyPage:
            object_list = paginator.page(1).object_list

        data = [
            {
                "id": loc.id,
                "cueanexo": loc.cueanexo,
                "id_fila": loc.id_fila,
                "escuela": loc.escuela,
                "sala": loc.sala,
                "turno": loc.turno,
                "nom_secc": loc.nom_secc,
                "tipo_secc": loc.tipo_secc,
                "total": loc.total,
                "total_var": loc.total_var,
                "menos_1_año": loc.menos_1_año,
                "un_año": loc.un_año,
                "dos_años": loc.dos_años,
                "tres_años": loc.tres_años,
                "cuatro_años": loc.cuatro_años,
                "cinco_años": loc.cinco_años,
                "seis_años": loc.seis_años,
                "total_disc": loc.total_disc,
                
            }
            for loc in object_list
        ]

        return JsonResponse({
            "draw": draw,
            "recordsTotal": total,
            "recordsFiltered": filtered,
            "data": data,
            "error_msg": "",
        }, 
        safe=False)


