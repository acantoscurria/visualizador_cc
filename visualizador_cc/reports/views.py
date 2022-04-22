from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from visualizador_cc.users.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from visualizador_cc.reports.models import MatricComunInicial

# Create your views here.


class MatricComunInicialIndexView(View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Matriculas"}
        return render(request, "reports/ra_matricula.html", context)


class MatricComunInicialListView(ListView):
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

        total = MatricComunInicial.objects.using(ra_selected).all().count()
        filtered = total
        matricula_comun_inicial = MatricComunInicial.objects.using(ra_selected).all()

        if search:
            matricula_comun_inicial = MatricComunInicial.objects.using(ra_selected).filter(
                Q(cueanexo__icontains=search)
            )
            total = matricula_comun_inicial.count()
            filtered = total

        # paginator
        paginator = Paginator(matricula_comun_inicial, length)

        page_number = start / length + 1

        try:
            object_list = paginator.page(page_number).object_list
        except PageNotAnInteger:
            object_list = paginator.page(1).object_list
        except EmptyPage:
            object_list = paginator.page(1).object_list

        data = [
            {
                "id":loc.id,
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
                "var_disc": loc.var_disc,
                "nom_est": loc.nom_est,
                "nro_est": loc.nro_est,
                "anio_creac_establec": loc.anio_creac_establec,
                "fecha_creac_establec": loc.fecha_creac_establec,
                "region": loc.region,
                "udt": loc.udt,
                "cui": loc.cui,
                "cua": loc.cua,
                "cuof": loc.cuof,
                "sector": loc.sector,
                "ambito": loc.ambito,
                "ref_loc": loc.ref_loc,
                "calle": loc.calle,
                "numero": loc.numero,
                "localidad": loc.localidad,
                "departamento": loc.departamento,
                "cod_postal": loc.cod_postal,
                "categoria": loc.categoria,
                "estado_est": loc.estado_est,
                "estado_loc": loc.estado_loc,
                "telefono_cod_area": loc.telefono_cod_area,
                "telefono_nro": loc.telefono_nro,
                "per_funcionamiento": loc.per_funcionamiento,
                "email_loc": loc.email_loc,
                                
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
