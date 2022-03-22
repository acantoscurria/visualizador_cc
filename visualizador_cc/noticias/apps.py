from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NoticiasConfig(AppConfig):
    name = "visualizador_cc.noticias"
    verbose_name = _("Noticias")

    def ready(self):
        try:
            import visualizador_cc.noticias.signals  # noqa F401
        except ImportError:
            pass