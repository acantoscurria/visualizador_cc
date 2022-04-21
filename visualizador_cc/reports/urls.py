from django.urls import path

from visualizador_cc.reports.views import (
    MatricComunInicialIndexView,
    MatricComunInicialListView,
)

app_name = "reports"
urlpatterns = [
    path(
        "MatricComunInicial",
        MatricComunInicialIndexView.as_view(),
        name="ra_matricula_index",
    ),
    path(
        "matric_comun_inicial_list/",
        MatricComunInicialListView.as_view(),
        name="ra_matricula_list",
    ),
]
