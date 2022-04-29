from django.urls import path, include
from .views import MapaList,DatosMapaList,Visualizador

urlpatterns = [
    path('', MapaList.as_view(), name='nuevo-mapa'),
    path('visualizador', Visualizador.as_view(), name='nuevo-mapa'),
    path('datos_padron/',DatosMapaList.as_view(),name='datos-padron'),
]