from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from .models import Noticia
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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

class Postear(PermissionRequiredMixin, CreateView):
    permission_required = 'noticias.add_noticia'
    model = 'Noticia'
    template_name = 'pages/postear.html'
    form_class = forms_noticias
    success_url = reverse_lazy('noticias:index')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

@login_required
@permission_required('noticias.view_noticia', raise_exception=True)
def abmNoticias(request):
    n = Noticia.objects.all()
    
    ctx = {}
    ctx['noticias'] = n
    return render(request, 'pages/noticias/abm.html', ctx)

@login_required
@permission_required('noticias.change_noticia', raise_exception=True)
def editarNoticia(request, pk):
    noticia = Noticia.objects.get (pk = pk)
    if request.method == "GET":
        form = forms_noticias(instance=noticia)
    else:
        form = forms_noticias(request.POST, instance=noticia)
        if form.is_valid():
            form.save()     
        return redirect("noticias:abm")
    return render(request, "pages/postear.html", {"form":form})

@login_required
@permission_required('noticias.delete_noticia', raise_exception=True)
def eliminarNoticia(request, pk):
    noticia = Noticia.objects.get (pk = pk)
    if request.method == "GET":
        noticia.delete()
        return redirect("noticias:abm")
    return render(request, "pages/noticias/eliminar.html", {"noticia":noticia})