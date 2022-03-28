# from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.


class IndexView(View):
    def get(self, request):
        # <view logic>
        # return HttpResponse('result')

        context = {"result": ""}
        return render(request, "reports/index.html", context)


class LocalizacionesView(View):
    def get(self, request):
        context = {"title": "Localizaciones"}
        return render(request, "reports/localizaciones.html", context)
