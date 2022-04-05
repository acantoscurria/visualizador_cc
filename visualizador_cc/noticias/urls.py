from django.urls import path
from . import views
# from .ajax import eliminar_noticia

app_name = 'noticias'

urlpatterns = [
    path("", views.mostrarNoticias, name="index"),
    path("postear/", views.Postear.as_view(), name="postear"),
    path("detalle/<int:pk>", views.noticiaCompleta, name="detalle"),
    path("abm/", views.abmNoticias, name="abm"),
    path("abm/editar/<int:pk>", views.editarNoticia, name="editar"),
    path("abm/eliminar/<int:pk>", views.eliminarNoticia, name="eliminar"),
]