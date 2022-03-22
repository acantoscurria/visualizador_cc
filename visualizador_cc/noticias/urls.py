from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path("postear/", views.Postear.as_view(), name="postear"),
    path("noticias/", views.mostrarNoticias, name="noticias"),
    path("detalle/", views.noticiaCompleta, name="detalle"),
    
]