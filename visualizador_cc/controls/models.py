
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

    def parse(self):
        return {
            "id": self.id,
            "tipo_ed": self.tipo_ed,
            "nivel": self.nivel,
            "cueanexo": self.cueanexo,
            "id_fila": self.id_fila,
            "escuela": self.escuela,
            "sala": self.sala,
            "turno": self.turno,
            "nom_secc": self.nom_secc,
            "tipo_secc": self.tipo_secc,
            "total": self.total,
            "total_var": self.total_var,
            "menos_1_año": self.menos_1_año,
            "un_año": self.un_año,
            "dos_años": self.dos_años,
            "tres_años": self.tres_años,
            "cuatro_años": self.cuatro_años,
            "cinco_años": self.cinco_años,
            "seis_años": self.seis_años,
            "total_disc": self.total_disc,            
        }

        


class ConMatricComunSecundaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_ed = models.TextField(blank=True, null=True)
    nivel = models.TextField(blank=True, null=True)
    cueanexo = models.CharField(max_length=255, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    escuela = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    total_var = models.IntegerField(blank=True, null=True)
    nivel_or = models.CharField(max_length=255, blank=True, null=True)
    edad_12 = models.IntegerField(blank=True, null=True)
    edad_13 = models.IntegerField(blank=True, null=True)
    edad_14 = models.IntegerField(blank=True, null=True)
    edad_15 = models.IntegerField(blank=True, null=True)
    edad_16 = models.IntegerField(blank=True, null=True)
    edad_17 = models.IntegerField(blank=True, null=True)
    total_rep = models.IntegerField(blank=True, null=True)
    var_rep = models.IntegerField(blank=True, null=True)
    nro_orden_pe = models.IntegerField(blank=True, null=True)
    año_est = models.CharField(max_length=255, blank=True, null=True)
    nom_div = models.CharField(max_length=255, blank=True, null=True)
    tipo_div = models.CharField(max_length=255, blank=True, null=True)
    orientacion = models.CharField(max_length=255, blank=True, null=True)
    edad_11_y_menos = models.IntegerField(blank=True, null=True)
    edad_18 = models.IntegerField(blank=True, null=True)
    edad_19 = models.IntegerField(blank=True, null=True)
    edad_25_y_mas = models.IntegerField(blank=True, null=True)
    edad_20_24 = models.IntegerField(blank=True, null=True)
    denom_pe = models.CharField(max_length=255, blank=True, null=True)
    total_disc = models.IntegerField(blank=True, null=True)
    var_disc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'con_matric_comun_secundaria'
        verbose_name_plural = "ConMatriculasComunSecundaria"
   
    def parse(self):
        return {
            "id": self.id,
            "tipo_ed": self.tipo_ed,
            "nivel": self.nivel,
            "cueanexo": self.cueanexo,
            "id_fila": self.id_fila,
            "escuela": self.escuela,              
        }
          
