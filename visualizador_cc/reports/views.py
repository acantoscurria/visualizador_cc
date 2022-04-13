from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from visualizador_cc.reports.models import RaLocalizacion

# Create your views here.


class RaLocalizacionesIndexView(View):
    def get(self, request):
        context = {"title": "Localizaciones"}
        return render(request, "reports/ra_localizaciones.html", context)


class RaLocalizacionesListView(ListView):
    def post(self, request, *args, **kwargs):
        return JsonResponse(self._datatables(request), safe=False)

    def _datatables(self, request):

        datatables = request.POST
        draw = int(datatables.get("draw"))
        start = int(datatables.get("start"))
        length = int(datatables.get("length"))

        search = datatables.get("search[value]")
        ra_selected = datatables.get("ra_selected")

        if ra_selected == "-1":

            return {
                "draw": draw,
                "recordsTotal": 0,
                "recordsFiltered": 0,
                "data": [],
                "error_msg": "",
            }

        # if(TRUE):

        #     return {
        #         'draw': draw,
        #         'recordsTotal': 0,
        #         'recordsFiltered': 0,
        #         'data': [],
        #         'error_msg': "Un error"
        #     }

        records_total = RaLocalizacion.objects.using(ra_selected).all().count()
        records_filtered = records_total
        localizaciones = RaLocalizacion.objects.using(ra_selected).all()

        if search:
            localizaciones = RaLocalizacion.objects.using(ra_selected).filter(
                Q(nombre__icontains=search) | Q(cueanexo__icontains=search)
            )
            records_total = localizaciones.count()
            records_filtered = records_total

        # paginator
        paginator = Paginator(localizaciones, length)

        page_number = start / length + 1

        try:
            object_list = paginator.page(page_number).object_list
        except PageNotAnInteger:
            object_list = paginator.page(1).object_list
        except EmptyPage:
            object_list = paginator.page(1).object_list

        data = [
            {
                "id_localizacion": loc.id_localizacion,
                "nombre": loc.nombre,
                "cueanexo": loc.cueanexo,
                "c_estado": loc.c_estado,
                "conflicto": "TRUE" if loc.conflicto else "FALSE",
                "codigo_jurisdiccional": loc.codigo_jurisdiccional,
                "sector": loc.sector,
                "responsable": loc.responsable,
                "localidad": loc.localidad,
                "ambito": loc.ambito,
                "departamento": loc.departamento,
                "telefono": loc.telefono,
                "carga_baja": loc.carga_baja,
            }
            for loc in object_list
        ]

        return {
            "draw": draw,
            "recordsTotal": records_total,
            "recordsFiltered": records_filtered,
            "data": data,
            "error_msg": "",
        }
