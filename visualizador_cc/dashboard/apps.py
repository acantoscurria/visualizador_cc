from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DashboardConfig(AppConfig):
    name = "visualizador_cc.dashboard"
    verbose_name = _("Tablero")

    def ready(self):
        try:
            import visualizador_cc.dashboard.signals  # noqa F401
        except ImportError:
            pass
