from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from visualizador_cc.reports.models import *

# Create your views here.

class ReportsMatricIndexView(View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Matriculas"}
        return render(request, "reports/ra_matricula.html", context)


class ReportsMatricListView(ListView):

    def post(self, request, *args, **kwargs):

        dt = request.POST   
        matricula_selected = dt.get("matricula_selected")    
        ra_selected = dt.get("ra_selected")     

        print('matricula_selected', matricula_selected)
        print('control_type_selected', ra_selected)

        if(matricula_selected == "none" or ra_selected == "none"):            
            return JsonResponse({ "data": [] }, safe=False)    

        if(matricula_selected == 'matricula_comun_inicial'):
            object_list = RepMatricComunInicial.objects.using(ra_selected).all()

        if(matricula_selected == 'matricula_comun_primaria'):   
            object_list = RepMatricComunPrimaria.objects.using(ra_selected).all()

        if(matricula_selected == 'matricula_comun_secundaria'):   
            object_list = RepMatricComunSecundaria.objects.using(ra_selected).all()
                
        if(matricula_selected == 'matricula_comun_snu'): 
            object_list = RepMatricComunSnu.objects.using(ra_selected).all()

        if(matricula_selected == 'matricula_adultos_primaria'): 
            object_list = RepMatricAdultosPrimaria.objects.using(ra_selected).all()
        
        if(matricula_selected == 'matricula_adultos_secundaria'):          
            object_list = RepMatricAdultosSecundaria.objects.using(ra_selected).all()
        
        if(matricula_selected == 'matricula_especial_inicial'): 
            object_list = RepMatricEspecialInicial.objects.using(ra_selected).all()
        
        if(matricula_selected == 'matricula_especial_primaria'):
            object_list = RepMatricEspecialPrimaria.objects.using(ra_selected).all()
             
        data = []  
        for row in object_list:
            # print('parse', row.parse())
            data.append(row.parse())

        return JsonResponse({"data": data}, safe=False) 
        