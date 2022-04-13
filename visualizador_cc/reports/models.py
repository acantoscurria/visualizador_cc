# from django.contrib.gis.db import models

from django.db import models


class RaLocalizacion(models.Model):
    id_localizacion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    cueanexo = models.CharField(unique=True, max_length=9, blank=True, null=True)
    c_estado = models.IntegerField()
    conflicto = models.BooleanField()
    codigo_jurisdiccional = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    responsable = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    ambito = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)
    carga_baja = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "localizacion"
        verbose_name_plural = "Localizaciones"

    def __str__(self):
        return f"{self.nombre}"
