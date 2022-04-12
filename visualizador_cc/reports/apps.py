from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReportsConfig(AppConfig):
    name = "visualizador_cc.reports"
    verbose_name = _("Reportes")

    def ready(self):
        try:
            import visualizador_cc.reports.signals  # noqa F401
        except ImportError:
            pass
