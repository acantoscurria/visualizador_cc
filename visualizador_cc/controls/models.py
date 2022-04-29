
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
    menos_1_anio = models.IntegerField(blank=True, null=True)
    un_anio = models.IntegerField(blank=True, null=True)
    dos_anios = models.IntegerField(blank=True, null=True)
    tres_anios = models.IntegerField(blank=True, null=True)
    cuatro_anios = models.IntegerField(blank=True, null=True)
    cinco_anios = models.IntegerField(blank=True, null=True)
    seis_anios = models.IntegerField(blank=True, null=True)
    total_disc = models.IntegerField(blank=True, null=True)
    var_disc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'con_matric_comun_inicial'
        verbose_name_plural = "ConMatriculasComunInicial"


    def __str__(self):
        return f"{self.escuela}"


  



class ConMatricComunPrimaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    tipo_ed = models.TextField(blank=True, null=True)
    nivel = models.TextField(blank=True, null=True)
    cueanexo = models.CharField(max_length=255, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    escuela = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    nombre_secc = models.CharField(max_length=255, blank=True, null=True)
    tipo_secc = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    total_var = models.IntegerField(blank=True, null=True)
    nivel_or = models.CharField(max_length=255, blank=True, null=True)
    grado_anio = models.CharField(max_length=255, blank=True, null=True)
    edad_5 = models.IntegerField(blank=True, null=True)
    edad_6 = models.IntegerField(blank=True, null=True)
    edad_7 = models.IntegerField(blank=True, null=True)
    edad_8 = models.IntegerField(blank=True, null=True)
    edad_9 = models.IntegerField(blank=True, null=True)
    edad_10 = models.IntegerField(blank=True, null=True)
    edad_11 = models.IntegerField(blank=True, null=True)
    edad_12 = models.IntegerField(blank=True, null=True)
    edad_13 = models.IntegerField(blank=True, null=True)
    edad_14 = models.IntegerField(blank=True, null=True)
    edad_15 = models.IntegerField(blank=True, null=True)
    edad_16 = models.IntegerField(blank=True, null=True)
    edad_17 = models.IntegerField(blank=True, null=True)
    edad_18_y_mas = models.IntegerField(blank=True, null=True)
    total_rep = models.IntegerField(blank=True, null=True)
    # var_rep = models.IntegerField(blank=True, null=True)
    tot_alum_promoasis = models.IntegerField(blank=True, null=True)
    var_alum_promoasis = models.IntegerField(blank=True, null=True)
    tot_discapacidad = models.IntegerField(blank=True, null=True)
    # var_discapacidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'con_matric_comun_primaria'
        verbose_name_plural = "ConMatriculasComunPrimaria"


    def __str__(self):
        return f"{self.escuela}"

          

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
    anio_est = models.CharField(max_length=255, blank=True, null=True)
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


    def __str__(self):
        return f"{self.escuela}"

   