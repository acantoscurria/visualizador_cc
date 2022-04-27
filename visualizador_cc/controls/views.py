

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
import pandas as pd

from visualizador_cc.controls.functions.controles import (
    MatriculaComunIncialControl,
    MatriculaComunPrimariaControl,
    MatriculaComunSecundariaControl
)


from visualizador_cc.controls.models import (
    ConMatricComunInicial,
    ConMatricComunPrimaria,
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
        matricula_selected = dt.get("matricula_selected")    
        control_type_selected = dt.get("control_type_selected")     

        print('matricula_selected', matricula_selected)
        print('control_type_selected', control_type_selected)

        if(matricula_selected == "none" or control_type_selected == "none"):            
            return JsonResponse({                      
                        "data": [],              
                    }, 
                    safe=False)    
            
            
        if(length != -1): #hay paginacion
            page_number = start / length + 1  

        if(matricula_selected == "matricula_comun_inicial"):
        
            if(control_type_selected == "precocidad"):

                df = pd.DataFrame(ConMatricComunInicial.objects.all().values())   
             
                df["error"] = df.apply(MatriculaComunIncialControl.precocidad, axis=1)            

                return JsonResponse({                    
                    "data": df.to_dict('records'),                   
                }, 
                safe=False)
                

            if(control_type_selected == "sobreedad"):
           
                df = pd.DataFrame(ConMatricComunInicial.objects.all().values())    

                df["error"] = df.apply(MatriculaComunIncialControl.sobreedad, axis=1)            
            
                return JsonResponse({                   
                    "data": df[df["error"] > 0].to_dict('records'),                
                }, 
                safe=False)

        if(matricula_selected == "matricula_comun_primaria"):
        
            if(control_type_selected == "precocidad"):

                df = pd.DataFrame(ConMatricComunPrimaria.objects.all().values())   
             
                df["error"] = df.apply(MatriculaComunPrimariaControl.precocidad, axis=1)            

                return JsonResponse({                    
                    "data": df[df["error"] > 0].to_dict('records'),                   
                }, 
                safe=False)
                

            if(control_type_selected == "sobreedad"):
           
                df = pd.DataFrame(ConMatricComunPrimaria.objects.all().values())    

                df["error"] = df.apply(MatriculaComunPrimariaControl.sobreedad, axis=1)            
            
                return JsonResponse({                    
                    "data": df[df["error"] > 0].to_dict('records'),                   
                }, 
                safe=False)

        if(matricula_selected == "matricula_comun_secundaria"):
        
            if(control_type_selected == "precocidad"):

                df = pd.DataFrame(ConMatricComunSecundaria.objects.all().values())   
             
                df["error"] = df.apply(MatriculaComunSecundariaControl.precocidad, axis=1)            

                return JsonResponse({                    
                    "data": df[df["error"] > 0].to_dict('records'),                   
                }, 
                safe=False)           


        return JsonResponse({               
                "data": [],           
            }, 
            safe=False)  
      
