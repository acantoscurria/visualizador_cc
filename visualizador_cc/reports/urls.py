from django.urls import path

from visualizador_cc.reports.views import (
    RaLocalizacionesIndexView,
    RaLocalizacionesListView,
)

app_name = "reports"
urlpatterns = [
    path(
        "RaLocalizaciones",
        RaLocalizacionesIndexView.as_view(),
        name="ra_localizaciones_index",
    ),
    path(
        "ra_localizaciones_list/",
        RaLocalizacionesListView.as_view(),
        name="ra_localizaciones_list",
    ),
]
