

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
import pandas as pd

from visualizador_cc.controls.models import (
    ConMatricComunInicial,
    ConMatricComunSecundaria
)
# Create your views here.


class ControlsMatriculaIndexView(View):
    def get(self, request):       
        context = {
            "title": "Control de Mátriculas - RA 2022",           
        }
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
        
            if(control_type_selected == "edades"):

                items = ConMatricComunInicial.objects.all()[:10].values()
                df = pd.DataFrame(items)    

                def control_precocidad(row):
                    if(row['sala'] == "Sala de 3 años"):
                        if(row["menos_1_año"] > 0
                            or row["un_año"] > 0
                                or row["dos_años"] > 0                               
                                   or row["cuatro_años"] > 0
                                        or row["cinco_años"] > 0
                                             or row["seis_años"] > 0):
                                                return 1

                    if(row['sala'] == "Sala de 4 años"):
                        if(row["menos_1_año"] > 0
                            or row["un_año"] > 0
                                or row["dos_años"] > 0                               
                                   or row["tres_años"] > 0
                                        or row["cinco_años"] > 0
                                             or row["seis_años"] > 0):
                                                return 1

                    if(row['sala'] == "Sala de 5 años"):
                        if(row["menos_1_año"] > 0
                            or row["un_año"] > 0
                                or row["dos_años"] > 0                               
                                   or row["tres_años"] > 0
                                        or row["cuatro_años"] > 0):
                                            #  or row["seis_años"] > 0):
                                            return 1


                    return 0
            

                # precodidad
                df["error"] = df.apply(control_precocidad, axis=1)

                # print('to_dict', df.to_dict('records'))

                data = df.to_dict('records')

                return JsonResponse({
                    "draw": draw,
                    "recordsTotal":  len(data),
                    "recordsFiltered":  len(data),
                    "data": data,
                    "error_msg": "",
                }, 
                safe=False)
                

  



      
