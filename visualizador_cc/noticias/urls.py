from django.urls import path
from . import views

app_name = 'noticias'

urlpatterns = [
    path("", views.mostrarNoticias, name="index"),
    path("postear/", views.Postear.as_view(), name="postear"),
    path("detalle/<int:pk>", views.noticiaCompleta, name="detalle"),
    
]