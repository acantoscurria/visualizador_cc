from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Noticia
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import forms_noticias

def mostrarNoticias(request):
    n = Noticia.objects.all()
    
    ctx = {}
    ctx['noticias'] = n
    return render(request, 'pages/noticias/index.html', ctx)

def noticiaCompleta(request, pk):
    noticia = Noticia.objects.get(pk = pk)
    
    ctx = {}
    ctx['complete_new'] = noticia
    

    return render(request, 'pages/noticias/detalle.html', ctx)

class Postear(LoginRequiredMixin, CreateView):
    model = 'Noticia'
    template_name = 'pages/postear.html'
    form_class = forms_noticias
    success_url = reverse_lazy('noticias:index')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
