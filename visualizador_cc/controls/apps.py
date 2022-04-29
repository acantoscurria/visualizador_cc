from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ControlsConfig(AppConfig):
    name = "visualizador_cc.controls"
    verbose_name = _("Correciones")

    def ready(self):
        try:
            import visualizador_cc.controls.signals  # noqa F401
        except ImportError:
            pass
