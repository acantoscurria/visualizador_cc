from django.urls import path

from . import views

app_name = "mapa"
urlpatterns = [
    path('mapa_general/', views.MapaGeneral.as_view(), name='mapa_general'),
    path('', views.Mapa.as_view(), name='index'),
    path('points/', views.Points.as_view(), name='points'),
    path('point_data/', views.PointData.as_view(),name='point_data'),
    path('search/', views.Search.as_view(), name='search'),
    path('filter/', views.Filter.as_view(),name='filter'),
    path('localizaciones_by_draw/', views.LocalizacionesByDraw.as_view(), name='localizaciones_by_draw'),
    path('localizaciones_by_draw_list/', views.LocalizacionesByDrawList.as_view(), name='localizaciones_by_draw_list'),
]