#
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = "dashboard/index.html"
    extra_context = { "title": "Cargos y horas 2021" }
