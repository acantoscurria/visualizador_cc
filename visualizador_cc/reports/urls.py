from django.urls import path

from visualizador_cc.reports.views import IndexView, LocalizacionesView

app_name = "reports"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("localizaciones", LocalizacionesView.as_view(), name="localizaciones"),
]
