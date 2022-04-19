from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from visualizador_cc.users.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from visualizador_cc.reports.models import RaLocalizacion

# Create your views here.


class RaLocalizacionesIndexView(View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Localizaciones"}
        return render(request, "reports/ra_localizaciones.html", context)


class RaLocalizacionesListView(ListView):
    def post(self, request, *args, **kwargs):
        return JsonResponse(self._datatables(request), safe=False)

    def _datatables(self, request):

        dt = request.POST
        draw = int(dt.get("draw"))
        start = int(dt.get("start"))
        length = int(dt.get("length"))

        search = dt.get("search[value]")
        ra_selected = dt.get("ra_selected")

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

        total = RaLocalizacion.objects.using(ra_selected).all().count()
        filtered = total
        localizaciones = RaLocalizacion.objects.using(ra_selected).all()

        if search:
            localizaciones = RaLocalizacion.objects.using(ra_selected).filter(
                Q(cueanexo__icontains=search)
            )
            total = localizaciones.count()
            filtered = total

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
                "cueanexo": loc.cueanexo,
                "nom_est": loc.nom_est,
                "nro_est": loc.nro_est,
                "region": loc.region
            }
            for loc in object_list
        ]

        return {
            "draw": draw,
            "recordsTotal": total,
            "recordsFiltered": filtered,
            "data": data,
            "error_msg": "",
        }
