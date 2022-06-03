from django.urls import path

from visualizador_cc.indicadores.views import (
    CargosHorasView,
    AnalisisComunInicialView
)
app_name = "indicadores"
urlpatterns = [
    path(
        "cargos-horas",
        CargosHorasView.as_view(),
        name="cargos_horas",
    ),
    path(
        "analisis-comun-inical/",
        AnalisisComunInicialView.as_view(),
        name="analisis_comun_inical",
    )
]
