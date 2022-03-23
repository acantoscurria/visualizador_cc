from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevo/', views.nuevo_mapa, name='nuevo-mapa'),
    path('datos_padron/',views.datosPadron,name='datos-padron'),
    path('datos_padron/<int:cueanexo>',views.datosPadron,name='datos-padron')
]