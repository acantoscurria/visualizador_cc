from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from visualizador_cc.users.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from visualizador_cc.reports.models import RepMatricComunInicial, RepMatricComunPrimaria, RepMatricComunSecundaria, RepMatricComunSnu, RepMatricAdultosPrimaria, RepMatricAdultosSecundaria, RepMatricEspecialInicial, RepMatricEspecialPrimaria

# Create your views here.


class ReportsMatricIndexView(View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Matriculas"}
        return render(request, "reports/ra_matricula.html", context)


class ReportsMatricListView(ListView):
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

        search = dt.get("search[value]")
        matricula_selected = dt.get("matricula_selected")    
        ra_selected = dt.get("ra_selected")     

        print('matricula_selected', matricula_selected)
        print('control_type_selected', ra_selected)

        if(matricula_selected == "none" or ra_selected == "none"):            
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": 0,
                        "recordsFiltered": 0,
                        "data": [],
                        "error_msg": "",
                    }, 
                    safe=False)    

        if(matricula_selected == 'matricula_comun_inicial'):   

            recordsTotal = RepMatricComunInicial.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricComunInicial.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricComunInicial.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricComunInicial.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricComunInicial.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricComunInicial.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricComunInicial.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        if(matricula_selected == 'matricula_comun_primaria'):   

            recordsTotal = RepMatricComunPrimaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricComunPrimaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricComunPrimaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricComunPrimaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricComunPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricComunPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricComunPrimaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        if(matricula_selected == 'matricula_comun_secundaria'):   

            recordsTotal = RepMatricComunSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricComunSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricComunSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricComunSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricComunSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricComunSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricComunSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(matricula_selected == 'matricula_comun_snu'):   

            recordsTotal = RepMatricComunSnu.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricComunSnu.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricComunSnu.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricComunSnu.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricComunSnu.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricComunSnu.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricComunSnu.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(matricula_selected == 'matricula_adultos_primaria'):   

            recordsTotal = RepMatricAdultosPrimaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricAdultosPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricAdultosPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricAdultosPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricAdultosPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricAdultosPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricAdultosPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(matricula_selected == 'matricula_adultos_secundaria'):   

            recordsTotal = RepMatricAdultosSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricAdultosSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricAdultosSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(matricula_selected == 'matricula_especial_inicial'):   

            recordsTotal = RepMatricEspecialInicial.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricEspecialInicial.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricEspecialInicial.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricEspecialInicial.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricEspecialInicial.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricEspecialInicial.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricEspecialInicial.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(matricula_selected == 'matricula_especial_primaria'):   

            recordsTotal = RepMatricEspecialInicial.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricEspecialPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricEspecialPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricEspecialPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricEspecialPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricEspecialPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricEspecialPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        data = []  
        for row in object_list:
            # print('parse', row.parse())
            data.append(row.parse())

        return JsonResponse({
            "draw": draw,
            "recordsTotal": recordsTotal,
            "recordsFiltered": recordsFiltered,
            "data": data,
            "error_msg": "",
        }, 
        safe=False)