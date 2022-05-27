from django.urls import path

from . import views

app_name = "mapa"
urlpatterns = [
    path('', views.Mapa.as_view(), name='index'),
    path('points/', views.Points.as_view(), name='points'),
    path('point_data/', views.PointData.as_view(),name='point_data'),
    path('search/', views.Search.as_view(), name='search'),
    path('filter/', views.Filter.as_view(),name='filter'),
    path('localizaciones_by_circle/', views.LocalizacionesByCircle.as_view(), name='localizaciones_by_circle'),
    path('localizaciones_by_circle_list/', views.LocalizacionesByCircleList.as_view(), name='localizaciones_by_circle_list'),
]