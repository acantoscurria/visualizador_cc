from django.urls import path
from .views import MapaPoints,PointData,Mapa

urlpatterns = [
    path('', Mapa.as_view(), name='mapa'),
    path('mapa_points/', MapaPoints.as_view(), name='mapa_points'),
    path('point_data/', PointData.as_view(),name='point_data'),
]