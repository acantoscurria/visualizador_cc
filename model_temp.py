PostgreSQL is available
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class ConMatricComunSecundaria(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    tipo_ed = models.TextField(blank=True, null=True)
    nivel = models.TextField(blank=True, null=True)
    cueanexo = models.CharField(max_length=-1, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    escuela = models.CharField(max_length=-1, blank=True, null=True)
    turno = models.CharField(max_length=-1, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    total_var = models.IntegerField(blank=True, null=True)
    nivel_or = models.CharField(max_length=-1, blank=True, null=True)
    edad_12 = models.IntegerField(blank=True, null=True)
    edad_13 = models.IntegerField(blank=True, null=True)
    edad_14 = models.IntegerField(blank=True, null=True)
    edad_15 = models.IntegerField(blank=True, null=True)
    edad_16 = models.IntegerField(blank=True, null=True)
    edad_17 = models.IntegerField(blank=True, null=True)
    total_rep = models.IntegerField(blank=True, null=True)
    var_rep = models.IntegerField(blank=True, null=True)
    nro_orden_pe = models.IntegerField(blank=True, null=True)
    año_est = models.CharField(max_length=-1, blank=True, null=True)
    nom_div = models.CharField(max_length=-1, blank=True, null=True)
    tipo_div = models.CharField(max_length=-1, blank=True, null=True)
    orientacion = models.CharField(max_length=-1, blank=True, null=True)
    edad_11_y_menos = models.IntegerField(blank=True, null=True)
    edad_18 = models.IntegerField(blank=True, null=True)
    edad_19 = models.IntegerField(blank=True, null=True)
    edad_25_y_mas = models.IntegerField(blank=True, null=True)
    edad_20_24 = models.IntegerField(blank=True, null=True)
    denom_pe = models.CharField(max_length=-1, blank=True, null=True)
    total_disc = models.IntegerField(blank=True, null=True)
    var_disc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'con_matric_comun_secundaria'
[0m