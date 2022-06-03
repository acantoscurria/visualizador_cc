from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.



class CargosHorasView(TemplateView):
    template_name = "indicadores/cargos_horas.html"
    extra_context = { "title": "Cargos y horas 2021" }

class AnalisisComunInicialView(TemplateView):
    template_name = "indicadores/analisis_comun_inicial.html"
    extra_context = { "title": "Análsis Común Inicial 2021" }

