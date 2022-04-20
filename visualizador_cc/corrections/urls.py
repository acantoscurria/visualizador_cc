from django.urls import path

from visualizador_cc.corrections.views import MatriculaIndexView

app_name = "corrections"
urlpatterns = [
    path(
        "MatriculaIndexView",
        MatriculaIndexView.as_view(),
        name="matricula_index",
    )
]
