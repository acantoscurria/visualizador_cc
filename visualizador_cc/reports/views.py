# from django.http import HttpResponse
from django.views.generic.list import ListView
from django.http import  JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from visualizador_cc.reports.models import RaLocalizacion


# Create your views here.


class RaLocalizacionesIndexView(View):
    def get(self, request):
        context = {"title": "Localizaciones"}
        return render(request, "reports/ra_localizaciones.html", context)



class RaLocalizacionesListView(ListView):
    model: RaLocalizacion

    def raLocalizacionToDictionary(raLoc):
        """
        A utility function to convert object of type RaLoc to a Python Dictionary
        """
        output = {}
        output["id_localizacion"] = raLoc.id_localizacion
        output["nombre"] = raLoc.nombre
        output["cueanexo"] = raLoc.cueanexo
        output["c_estado"] = raLoc.c_estado
        output["conflicto"] = raLoc.conflicto
        output["codigo_jurisdiccional"] = raLoc.codigo_jurisdiccional
        output["sector"] = raLoc.sector
        output["responsable"] = raLoc.responsable
        output["localidad"] = raLoc.localidad
        output["ambito"] = raLoc.ambito
        output["departamento"] = raLoc.departamento
        output["telefono"] = raLoc.telefono
        output["carga_baja"] = raLoc.carga_baja

        return output


    def get_queryset(self):
        return self.model.objects.using('ra2021').all()

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            temp = []
            raLocalizaciones = self.get_queryset()
            for i in range(len(raLocalizaciones)):
                temp.append(self.raLocalizacionToDictionary(raLocalizaciones[i])) # Converting `QuerySet` to a Python Dictionary
            raLocalizaciones = temp
            return JsonResponse(raLocalizaciones)
        else:
            return redirect('reportes:index')
