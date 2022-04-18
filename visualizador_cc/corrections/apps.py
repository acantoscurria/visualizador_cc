from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CorrectionsConfig(AppConfig):
    name = "visualizador_cc.corrections"
    verbose_name = _("Correciones")

    def ready(self):
        try:
            import visualizador_cc.corrections.signals  # noqa F401
        except ImportError:
            pass
