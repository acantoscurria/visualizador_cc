from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IndicadoresConfig(AppConfig):
    name = "visualizador_cc.indicadores"
    verbose_name = _("Correciones")

    def ready(self):
        try:
            import visualizador_cc.indicadores.signals  # noqa F401
        except ImportError:
            pass
