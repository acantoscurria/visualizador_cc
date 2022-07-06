from unicodedata import name
from django.urls import path

from visualizador_cc.reports.views.matriculas import (
    ReportsMatricIndexView,
    ReportsMatricListView
)


from visualizador_cc.reports.viewsOLD import *



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
    ),
    path(
        "ReportCargosIndexView",
        ReportCargosIndexView.as_view(),
        name="ra_cargos_index"
    ),
    path(
        "ra_cargos_list/",
        ReportCargosListView.as_view(),
        name="ra_cargos_list"
    ),

    path(
        'ra_cargos_options/',
         CargosOptionsList.as_view(),
         name='ra_cargos_options'
    ),

    path(
        "ReportSeccionesIndexView",
        ReportSeccionesIndexView.as_view(),
        name="ra_secciones_index"
    ),
    path(
        "ra_secciones_list/",
        ReportSeccionesListView.as_view(),
        name="ra_secciones_list"
    ),
    path(
        "ReportHorasIndexView",
        ReportHorasIndexView.as_view(),
        name="ra_horas_catedra_index"
    ),
    path(
        "ra_horas_catedra_list/",
        ReportHorasListView.as_view(),
        name="ra_horas_catedra_list"
    ),
    path(
        "ReportEgresadosIndexView",
        ReportEgresadosIndexView.as_view(),
        name="ra_egresados_index"
    ),
    path(
        "ra_egresados_list/",
        ReportEgresadosListView.as_view(),
        name="ra_egresados_list"
    ),
    path(
        "ReportJornadaIndexView",
        ReportJornadaIndexView.as_view(),
        name="ra_jornada_index"
    ),
    path(
        "ra_jornada_list/",
        ReportJornadaListView.as_view(),
        name="ra_jornada_list"
    )
]
