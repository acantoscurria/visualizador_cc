from django.urls import path

from visualizador_cc.reports.views import (
    ReportsMatricIndexView,
    ReportsMatricListView,
)

app_name = "reports"
urlpatterns = [
    path(
        "RepMatricComunInicial",
        ReportsMatricIndexView.as_view(),
        name="ra_matricula_index",
    ),
    path(
        "matric_comun_inicial_list/",
        ReportsMatricListView.as_view(),
        name="ra_matricula_list",
    ),
]
