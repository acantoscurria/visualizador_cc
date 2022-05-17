from django.urls import path
from .views import Points,PointData,Mapa, Search,SpatialQuery,Filter

app_name = "mapa"
urlpatterns = [
    path('', Mapa.as_view(), name='index'),
    path('points/', Points.as_view(), name='points'),
    path('point_data/', PointData.as_view(),name='point_data'),
    path('search/', Search.as_view(), name='search'),
    path('spatialquery/', SpatialQuery.as_view(), name='spatialquery'),
    path('filter/', Filter.as_view(),name='filter'),
]