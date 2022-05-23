from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from visualizador_cc.users.models import User
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from visualizador_cc.reports.models import *

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
        
class ReportLocalizacionesIndexView(View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Localizaciones"}
        return render(request, "reports/ra_localizaciones.html", context)
    
class ReportMatricAborigenIndexView(View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Matricula Aborigen"}
        return render(request, "reports/ra_matricula_aborigen.html", context)
    
class ReportMatricAborigenListView(ListView):
    def post(self, request, *args, **kwargs):
        dt=request.POST
        draw = int(dt.get("draw"))
        start = int(dt.get("start"))
        length = int(dt.get("length"))
        
        print('start', start)
        print('length', length)

        recordsTotal = 0
        data = []
        recordsFiltered = 0

        search = dt.get("search[value]")
        ra_selected = dt.get("ra_selected")
        
        print('control_type_selected', ra_selected)
        
        if(ra_selected == "none"):
            return JsonResponse({
                "draw": draw,
                "recordsTotal": 0,
                "recordsFiltered": 0,
                "data": [],
                "error_msg": "",
            }, 
            safe=False)
        else:
            recordsTotal = RepMatricAborigen.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepMatricAborigen.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepMatricAborigen.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepMatricAborigen.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepMatricAborigen.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepMatricAborigen.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepMatricAborigen.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
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
        
class ReportTrayectoriaIndexView(View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Trayectoria"}
        return render(request, "reports/ra_trayectoria.html", context)
    
class ReportTrayectoriaListView(ListView):
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
        nivel_selected = dt.get("nivel_selected")    
        ra_selected = dt.get("ra_selected")     

        print('nivel_selected', nivel_selected)
        print('control_type_selected', ra_selected)

        if(nivel_selected == "none" or ra_selected == "none"):            
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": 0,
                        "recordsFiltered": 0,
                        "data": [],
                        "error_msg": "",
                    }, 
                    safe=False)    
            
        if(nivel_selected == 'trayectoria_comun_primaria'):   

            recordsTotal = RepTrayectoriaPrimaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepTrayectoriaPrimaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepTrayectoriaPrimaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepTrayectoriaPrimaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepTrayectoriaPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepTrayectoriaPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepTrayectoriaPrimaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
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
        
class ReportDocenteActividadIndexView (View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Docentes en Actividad"}
        return render(request, "reports/ra_docentes_actividad.html", context)

class ReportDocenteActividadListView (ListView):
    def post(self, request, *args, **kwargs):
        dt=request.POST
        draw = int(dt.get("draw"))
        start = int(dt.get("start"))
        length = int(dt.get("length"))
        
        print('start', start)
        print('length', length)

        recordsTotal = 0
        data = []
        recordsFiltered = 0

        search = dt.get("search[value]")
        ra_selected = dt.get("ra_selected")
        
        print('control_type_selected', ra_selected)
        
        if(ra_selected == "none"):
            return JsonResponse({
                "draw": draw,
                "recordsTotal": 0,
                "recordsFiltered": 0,
                "data": [],
                "error_msg": "",
            }, 
            safe=False)
        else:
            recordsTotal = RepDocenteActividad.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepDocenteActividad.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepDocenteActividad.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepDocenteActividad.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepDocenteActividad.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepDocenteActividad.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepDocenteActividad.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
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
        
class ReportCargosIndexView (View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Cargos"}
        return render(request, "reports/ra_cargos.html", context)
    
class ReportCargosListView (ListView):
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
        nivel_oferta_selected = dt.get("nivel_oferta_selected")    
        ra_selected = dt.get("ra_selected")     

        print('nivel_oferta_selected', nivel_oferta_selected)
        print('control_type_selected', ra_selected)

        if(nivel_oferta_selected == "None" or ra_selected == "none"):     
            
            print('Salida por None')
                   
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": 0,
                        "recordsFiltered": 0,
                        "data": [],
                        "error_msg": "",
                    }, 
                    safe=False)    

        if(nivel_oferta_selected == 'comun_inicial_maternal'):   

            recordsTotal = RepCargosComunInicialMaternal.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosComunInicialMaternal.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosComunInicialMaternal.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosComunInicialMaternal.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosComunInicialMaternal.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosComunInicialMaternal.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosComunInicialMaternal.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        if(nivel_oferta_selected == 'comun_inicial_jardin'):   

            recordsTotal = RepCargosComunInicialJardin.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosComunInicialJardin.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosComunInicialJardin.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosComunInicialJardin.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosComunInicialJardin.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosComunInicialJardin.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosComunInicialJardin.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        if(nivel_oferta_selected == 'comun_primaria'):   

            recordsTotal = RepCargosComunPrimaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosComunPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosComunPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosComunPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosComunPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosComunPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosComunPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'comun_secundaria'):   

            recordsTotal = RepCargosComunSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosComunSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosComunSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosComunSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosComunSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosComunSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosComunSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(nivel_oferta_selected == 'comun_snu'):   

            recordsTotal = RepCargosComunSnu.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosComunSnu.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosComunSnu.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosComunSnu.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosComunSnu.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosComunSnu.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosComunSnu.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(nivel_oferta_selected == 'comun_artistica'):   

            recordsTotal = RepCargosComunArtistica.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosComunArtistica.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosComunArtistica.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosComunArtistica.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosComunArtistica.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosComunArtistica.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosComunArtistica.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(nivel_oferta_selected == 'comun_servicios_complementarios'):   

            recordsTotal = RepCargosComunServiciosComplementarios.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosComunServiciosComplementarios.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosComunServiciosComplementarios.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosComunServiciosComplementarios.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosComunServiciosComplementarios.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosComunServiciosComplementarios.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosComunServiciosComplementarios.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(nivel_oferta_selected == 'adultos_primaria'):   

            recordsTotal = RepCargosAdultosPrimaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosAdultosPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosAdultosPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosAdultosPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosAdultosPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosAdultosPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosAdultosPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'adultos_form_prof'):   

            recordsTotal = RepCargosAdultosFormProf.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosAdultosFormProf.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosAdultosFormProf.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosAdultosFormProf.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosAdultosFormProf.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosAdultosFormProf.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosAdultosFormProf.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'adultos_secundaria'):   

            recordsTotal = RepCargosAdultosSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosAdultosSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosAdultosSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'especial'):   

            recordsTotal = RepCargosEspecial.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepCargosEspecial.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepCargosEspecial.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepCargosEspecial.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepCargosEspecial.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepCargosEspecial.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepCargosEspecial.objects.using(ra_selected).filter(
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
        
class ReportSeccionesIndexView (View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Secciones"}
        return render(request, "reports/ra_secciones.html", context)
    
class ReportSeccionesListView (ListView):
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
        nivel_oferta_selected = dt.get("nivel_oferta_selected")    
        ra_selected = dt.get("ra_selected")     

        print('nivel_oferta_selected', nivel_oferta_selected)
        print('control_type_selected', ra_selected)

        if(nivel_oferta_selected == "None" or ra_selected == "none"):     
            
            print('Salida por None')
                   
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": 0,
                        "recordsFiltered": 0,
                        "data": [],
                        "error_msg": "",
                    }, 
                    safe=False)    
        
        if(nivel_oferta_selected == 'comun'):   

            recordsTotal = RepSeccionesComun.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepSeccionesComun.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepSeccionesComun.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepSeccionesComun.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepSeccionesComun.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepSeccionesComun.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepSeccionesComun.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()
        if(nivel_oferta_selected == 'adultos'):   

            recordsTotal = RepSeccionesAdultos.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepSeccionesAdultos.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepSeccionesAdultos.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepSeccionesAdultos.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepSeccionesAdultos.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepSeccionesAdultos.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepSeccionesAdultos.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()
        if(nivel_oferta_selected == 'form_prof'):   

            recordsTotal = RepSeccionesFormProf.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepSeccionesFormProf.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepSeccionesFormProf.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepSeccionesFormProf.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepSeccionesFormProf.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepSeccionesFormProf.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepSeccionesFormProf.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
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
        
class ReportHorasIndexView (View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Horas Cátedra"}
        return render(request, "reports/ra_horas_catedra.html", context)
    
class ReportHorasListView (ListView):
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
        nivel_oferta_selected = dt.get("nivel_oferta_selected")    
        ra_selected = dt.get("ra_selected")     

        print('nivel_oferta_selected', nivel_oferta_selected)
        print('control_type_selected', ra_selected)

        if(nivel_oferta_selected == "None" or ra_selected == "none"):     
            
            print('Salida por None')
                   
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": 0,
                        "recordsFiltered": 0,
                        "data": [],
                        "error_msg": "",
                    }, 
                    safe=False)    

        if(nivel_oferta_selected == 'comun_inicial_maternal'):   

            recordsTotal = RepHorasInicialMaternal.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasInicialMaternal.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasInicialMaternal.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasInicialMaternal.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasInicialMaternal.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasInicialMaternal.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasInicialMaternal.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        if(nivel_oferta_selected == 'comun_inicial_jardin'):   

            recordsTotal = RepHorasInicialJardin.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasInicialJardin.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasInicialJardin.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasInicialJardin.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasInicialJardin.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasInicialJardin.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasInicialJardin.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

        if(nivel_oferta_selected == 'comun_primaria'):   

            recordsTotal = RepHorasComunPrimaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasComunPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasComunPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasComunPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasComunPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasComunPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasComunPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'comun_secundaria'):   

            recordsTotal = RepHorasComunSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasComunSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasComunSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasComunSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasComunSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasComunSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasComunSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(nivel_oferta_selected == 'comun_snu'):   

            recordsTotal = RepHorasComunSnu.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasComunSnu.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasComunSnu.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasComunSnu.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasComunSnu.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasComunSnu.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasComunSnu.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'comun_servicios_complementarios'):   

            recordsTotal = RepHorasComunServiciosComplementarios.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasComunServiciosComplementarios.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasComunServiciosComplementarios.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasComunServiciosComplementarios.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasComunServiciosComplementarios.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasComunServiciosComplementarios.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasComunServiciosComplementarios.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
        
        if(nivel_oferta_selected == 'adultos_primaria'):   

            recordsTotal = RepHorasAdultosPrimaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasAdultosPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasAdultosPrimaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasAdultosPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasAdultosPrimaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasAdultosPrimaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasAdultosPrimaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'adultos_form_prof'):   

            recordsTotal = RepHorasAdultosFormProf.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasAdultosFormProf.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasAdultosFormProf.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasAdultosFormProf.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasAdultosFormProf.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasAdultosFormProf.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasAdultosFormProf.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'adultos_secundaria'):   

            recordsTotal = RepHorasAdultosSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasAdultosSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasAdultosSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()
                
        if(nivel_oferta_selected == 'especial'):   

            recordsTotal = RepHorasEspecial.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepHorasEspecial.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepHorasEspecial.objects.using(ra_selected).filter(
                        Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepHorasEspecial.objects.using(ra_selected).filter(
                    Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepHorasEspecial.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepHorasEspecial.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepHorasEspecial.objects.using(ra_selected).filter(
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
        
class ReportEgresadosIndexView (View, LoginRequiredMixin):
    def get(self, request):
        context = {"title": "Reporte Egresados"}
        return render(request, "reports/ra_egresados.html", context)

class ReportEgresadosListView (ListView):
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
        nivel_oferta_selected = dt.get("nivel_oferta_selected")    
        ra_selected = dt.get("ra_selected")     

        print('nivel_oferta_selected', nivel_oferta_selected)
        print('control_type_selected', ra_selected)

        if(nivel_oferta_selected == "None" or ra_selected == "none"):     
            
            print('Salida por None')
                   
            return JsonResponse({
                        "draw": draw,
                        "recordsTotal": 0,
                        "recordsFiltered": 0,
                        "data": [],
                        "error_msg": "",
                    }, 
                    safe=False)    
        
        if(nivel_oferta_selected == 'comun_secundaria'):   

            recordsTotal = RepEgresadosComunSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepEgresadosComunSecundaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepEgresadosComunSecundaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepEgresadosComunSecundaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepEgresadosComunSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepEgresadosComunSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepEgresadosComunSecundaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()
        if(nivel_oferta_selected == 'adultos_secundaria'):   

            recordsTotal = RepEgresadosAdultosSecundaria.objects.using(ra_selected).all().count()

            if search: # si hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas filtradas y paginado
                    object_list = RepEgresadosAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )[start:start + length]

                else:

                    # obtengo todas las filas filtradas sin paginacion
                    object_list = RepEgresadosAdultosSecundaria.objects.using(ra_selected).filter(
                        Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                    )

                # obtengo la cantidad de filas filtrdas sin paginacion
                recordsFiltered = RepEgresadosAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()

            else: # no hay valor de busqueda

                if(length != -1): #hay paginacion

                    # obtengo todas las filas con paginacion
                    object_list = RepEgresadosAdultosSecundaria.objects.using(ra_selected).all()[start:start + length]

                else:

                    # obtengo todas las filas sin paginacion
                    object_list = RepEgresadosAdultosSecundaria.objects.using(ra_selected).all()


                # obtengo la cantidad de filas sin paginacion
                recordsFiltered = RepEgresadosAdultosSecundaria.objects.using(ra_selected).filter(
                    Q(escuela__icontains=search) | Q(cueanexo__icontains=search)
                ).count()
        if(nivel_oferta_selected == 'snu'):   
            None
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
        
class ReportJornadaIndexView (View, LoginRequiredMixin):