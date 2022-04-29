from django.urls import path

from visualizador_cc.controls.views import (
    ControlsMatriculaIndexView,
    ControlsMatriculaListView    
)
app_name = "controls"
urlpatterns = [
    path(
        "MatriculaIndexView",
        ControlsMatriculaIndexView.as_view(),
        name="matricula_index",
    ),
    path(
        "matricula_list/",
        ControlsMatriculaListView.as_view(),
        name="matricula_list",
    )
]
