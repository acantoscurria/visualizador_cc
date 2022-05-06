from django.urls import path
from .views import Points,PointData,Mapa, SearchByName, SearchByCueanexo

app_name = "mapa"
urlpatterns = [
    path('', Mapa.as_view(), name='index'),
    path('points/', Points.as_view(), name='points'),
    path('point_data/', PointData.as_view(),name='point_data'),
    path('search_by_name/', SearchByName.as_view(), name='search_by_name'),
    path('search_by_cueanexo/', SearchByCueanexo.as_view(), name='search_by_cueanexo'),
]