
# from django.contrib.gis.db import models

from django.db import models

class ConMatricComunInicial(models.Model):
  
    id = models.BigIntegerField(primary_key=True)
    tipo_ed = models.TextField(blank=True, null=True)
    nivel = models.TextField(blank=True, null=True)
    cueanexo = models.CharField(max_length=255, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    escuela = models.CharField(max_length=255, blank=True, null=True)
    sala = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    nom_secc = models.CharField(max_length=255, blank=True, null=True)
    tipo_secc = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    total_var = models.IntegerField(blank=True, null=True)
    menos_1_año = models.IntegerField(blank=True, null=True)
    un_año = models.IntegerField(blank=True, null=True)
    dos_años = models.IntegerField(blank=True, null=True)
    tres_años = models.IntegerField(blank=True, null=True)
    cuatro_años = models.IntegerField(blank=True, null=True)
    cinco_años = models.IntegerField(blank=True, null=True)
    seis_años = models.IntegerField(blank=True, null=True)
    total_disc = models.IntegerField(blank=True, null=True)
    var_disc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'con_matric_comun_inicial'
        verbose_name_plural = "ConMatriculasComunInicial"


    def __str__(self):
        return f"{self.escuela}"

