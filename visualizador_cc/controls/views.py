

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
        show_all = dt.get("show_all")

        print('matricula_selected', matricula_selected)
        print('control_type_selected', control_type_selected)
        print('show_all', show_all)

        if(matricula_selected == "none" or control_type_selected == "none"):            
            return JsonResponse({                      
                        "data": [],              
                    }, 
                    safe=False)    

        if(matricula_selected == "matricula_comun_inicial"):

            df = pd.DataFrame(ConMatricComunInicial.objects.all().values()) 
        
            if(control_type_selected == "precocidad"): 
             
                df["control"] = df.apply(MatriculaComunIncialControl.precocidad, axis=1)  
             
            if(control_type_selected == "sobreedad"):

                df["control"] = df.apply(MatriculaComunIncialControl.sobreedad, axis=1)            
            
        if(matricula_selected == "matricula_comun_primaria"):

            df = pd.DataFrame(ConMatricComunPrimaria.objects.all().values()) 
        
            if(control_type_selected == "precocidad"):
             
                df["control"] = df.apply(MatriculaComunPrimariaControl.precocidad, axis=1)    

            if(control_type_selected == "sobreedad"):           

                df["control"] = df.apply(MatriculaComunPrimariaControl.sobreedad, axis=1)                

            if(control_type_selected == "repitencia"):           

                df["control"] = df.apply(MatriculaComunPrimariaControl.repitencia, axis=1)                


        if(matricula_selected == "matricula_comun_secundaria"):

            df = pd.DataFrame(ConMatricComunSecundaria.objects.all().values()) 
        
            if(control_type_selected == "precocidad"):                  
             
                df["control"] = df.apply(MatriculaComunSecundariaControl.precocidad, axis=1)  
                
            if(control_type_selected == "sobreedad"):

                df["control"] = df.apply(MatriculaComunSecundariaControl.sobreedad, axis=1)  


        if show_all == 'false':            
            data = df[df["control"] > 0].to_dict('records') 
        else:
            data = df.to_dict('records')          
    
        return JsonResponse({                    
            "data": data                
        }, 
        safe=False)