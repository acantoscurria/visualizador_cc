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
    model = RaLocalizacion

    def get_queryset(self):
        return (
            self.model.objects.using("ra2021")
            .all()
            .values("id_localizacion", "nombre", "cueanexo")
        )

    def get(self, request, *args, **kwargs):

        print("request.GET draw")
        print(request.GET.get("draw"))

        # print('request.GET columns')
        # print(request.GET.get('columns[]'))

        print("request.GET order")
        print(request.GET.get("order"))

        print("request.GET start")
        print(request.GET.get("start"))

        print("request.GET length")
        print(request.GET.get("length"))

        print("request.GET search")
        print(request.GET.get("search"))

        print("request.GET ra")
        print(request.GET.get("ra"))

        raLocalizaciones = self.get_queryset()
        data = list(raLocalizaciones)
        value = JsonResponse(
            {
                "data": data,
                "draw": request.GET.get("draw"),
                "recordsTotal": 5,
                "recordsFiltered": 5,
            },
            safe=False,
        )
        print(value)
        return value
