from unicodedata import name
from django.urls import path

from visualizador_cc.reports.views import (
    ReportsMatricIndexView,
    ReportsMatricListView,
    ReportLocalizacionesIndexView,
    ReportMatricAborigenIndexView,
    ReportMatricAborigenListView,
    ReportTrayectoriaIndexView,
    ReportTrayectoriaListView,
    ReportDocenteActividadIndexView,
    ReportDocenteActividadListView
)

app_name = "reports"
urlpatterns = [
    path(
        "ReportsMatricIndexView",
        ReportsMatricIndexView.as_view(),
        name="ra_matricula_index",
    ),
    path(
        "ra_matricula_list/",
        ReportsMatricListView.as_view(),
        name="ra_matricula_list",
    ),
    path(
        "ReportLocalizacionesIndexView",
        ReportLocalizacionesIndexView.as_view(),
        name="ra_localizaciones_index"
    ),
    path(
        "ReportMatricAborigenIndexView",
        ReportMatricAborigenIndexView.as_view(),
        name="ra_matricula_aborigen"
    ),
    path(
        "ra_matricula_aborigen_list/",
        ReportMatricAborigenListView.as_view(),
        name="ra_matricula_aborigen_list"
    ),
    path(
        "ReportTrayectoriaIndexView",
        ReportTrayectoriaIndexView.as_view(),
        name="ra_trayectoria_index"
    ),
    path(
        "ra_trayectoria_list/",
        ReportTrayectoriaListView.as_view(),
        name="ra_trayectoria_list"
    ),
    path(
        "ReportDocenteActividadIndexView",
        ReportDocenteActividadIndexView.as_view(),
        name="ra_docentes_actividad_index"
    ),
    path(
        "ra_docentes_actividad_list/",
        ReportDocenteActividadListView.as_view(),
        name="ra_docentes_actividad_list"
    )
]
