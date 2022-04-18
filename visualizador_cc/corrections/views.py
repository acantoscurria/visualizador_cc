from django.shortcuts import render
from django.views import View

# Create your views here.


class MatriculaIndexView(View):
    def get(self, request):
        context = {"title": "Mátricula"}
        return render(request, "corrections/matricula.html", context)
