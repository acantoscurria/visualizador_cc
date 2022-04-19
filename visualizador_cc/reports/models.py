# from django.contrib.gis.db import models

from django.db import models


class RaLocalizacion(models.Model):
    cueanexo = models.CharField(unique=True, max_length=9, blank=True, null=True)
    nom_est = models.CharField(max_length=50, blank=True, null=True)
    nro_est = models.CharField(max_length=5, blank=True, null=True)
    region = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "loc_region"
        verbose_name_plural = "Localizaciones"

    def __str__(self):
        return f"{self.nom_est}"
