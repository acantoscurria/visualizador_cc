from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MapaConfig(AppConfig):
    name = "visualizador_cc.mapa"
    verbose_name = _("Mapa")

    def ready(self):
        try:
            import visualizador_cc.mapa.signals  # noqa F401
        except ImportError:
            pass