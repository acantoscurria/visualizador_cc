# from django.contrib.gis.db import models

from django.db import models

class RepMatricComunInicial(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
    nom_est = models.CharField(max_length=255, blank=True, null=True)
    nro_est = models.CharField(max_length=255, blank=True, null=True)
    anio_creac_establec = models.CharField(max_length=255, blank=True, null=True)
    fecha_creac_establec = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    udt = models.CharField(max_length=255, blank=True, null=True)
    cui = models.CharField(max_length=255, blank=True, null=True)
    cua = models.CharField(max_length=255, blank=True, null=True)
    cuof = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    ambito = models.CharField(max_length=255, blank=True, null=True)
    ref_loc = models.CharField(max_length=255, blank=True, null=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    cod_postal = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    estado_est = models.CharField(max_length=255, blank=True, null=True)
    estado_loc = models.CharField(max_length=255, blank=True, null=True)
    telefono_cod_area = models.CharField(max_length=255, blank=True, null=True)
    telefono_nro = models.CharField(max_length=255, blank=True, null=True)
    per_funcionamiento = models.CharField(max_length=255, blank=True, null=True)
    email_loc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'matric_comun_inicial'

 
    def parse(self):
        return {
           "id":self.id,
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
            "var_disc": self.var_disc,
            "nom_est": self.nom_est,
            "nro_est": self.nro_est,
            "anio_creac_establec": self.anio_creac_establec,
            "fecha_creac_establec": self.fecha_creac_establec,
            "region": self.region,
            "udt": self.udt,
            "cui": self.cui,
            "cua": self.cua,
            "cuof": self.cuof,
            "sector": self.sector,
            "ambito": self.ambito,
            "ref_loc": self.ref_loc,
            "calle": self.calle,
            "numero": self.numero,
            "localidad": self.localidad,
            "departamento": self.departamento,
            "cod_postal": self.cod_postal,
            "categoria": self.categoria,
            "estado_est": self.estado_est,
            "estado_loc": self.estado_loc,
            "telefono_cod_area": self.telefono_cod_area,
            "telefono_nro": self.telefono_nro,
            "per_funcionamiento": self.per_funcionamiento,
            "email_loc": self.email_loc,            
        }
          
class RepMatricComunSecundaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cueanexo = models.CharField(max_length=255, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    escuela = models.CharField(max_length=255, blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    nombre_secc = models.CharField(max_length=255, blank=True, null=True)
    tipo_secc = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    total_var = models.IntegerField(blank=True, null=True)
    nivel = models.CharField(max_length=255, blank=True, null=True)
    grado_año = models.CharField(max_length=255, blank=True, null=True)
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
    var_rep = models.IntegerField(blank=True, null=True)
    tot_alum_promoasis = models.IntegerField(blank=True, null=True)
    var_alum_promoasis = models.IntegerField(blank=True, null=True)
    tot_discapacidad = models.IntegerField(blank=True, null=True)
    var_discapacidad = models.IntegerField(blank=True, null=True)
    nom_est = models.CharField(max_length=255, blank=True, null=True)
    nro_est = models.CharField(max_length=255, blank=True, null=True)
    anio_creac_establec = models.CharField(max_length=255, blank=True, null=True)
    fecha_creac_establec = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    udt = models.CharField(max_length=255, blank=True, null=True)
    cui = models.CharField(max_length=255, blank=True, null=True)
    cua = models.CharField(max_length=255, blank=True, null=True)
    cuof = models.CharField(max_length=255, blank=True, null=True)
    sector = models.CharField(max_length=255, blank=True, null=True)
    ambito = models.CharField(max_length=255, blank=True, null=True)
    ref_loc = models.CharField(max_length=255, blank=True, null=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=255, blank=True, null=True)
    localidad = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.CharField(max_length=255, blank=True, null=True)
    cod_postal = models.CharField(max_length=255, blank=True, null=True)
    categoria = models.CharField(max_length=255, blank=True, null=True)
    estado_est = models.CharField(max_length=255, blank=True, null=True)
    estado_loc = models.CharField(max_length=255, blank=True, null=True)
    telefono_cod_area = models.CharField(max_length=255, blank=True, null=True)
    telefono_nro = models.CharField(max_length=255, blank=True, null=True)
    per_funcionamiento = models.CharField(max_length=255, blank=True, null=True)
    email_loc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'matric_comun_secundaria'

    def parse(self):
        return {
            'id': self.id,
            'cueanexo': self.cueanexo,
            'id_fila': self.id_fila,
            'escuela': self.escuela,
            'turno': self.turno,
            'nombre_secc': self.nombre_secc,
            'tipo_secc': self.tipo_secc,
            'total': self.total,
            'total_var': self.total_var,
            'nivel': self.nivel,
            'grado_año': self.grado_año,
            'edad_5': self.edad_5,
            'edad_6': self.edad_6,
            'edad_7': self.edad_7,
            'edad_8': self.edad_8,
            'dad_9': self.edad_9,
            'edad_10': self.edad_10,
            'edad_11': self.edad_11,
            'edad_12': self.edad_12,
            'edad_13': self.edad_13,
            'edad_14': self.edad_14,
            'edad_15': self.edad_15,
            'edad_16': self.edad_16,
            'edad_17': self.edad_17,
            'edad_18_y_mas': self.edad_18_y_mas,
            'total_rep': self.total_rep,
            'var_rep': self.var_rep,
            'tot_alum_promoasis': self.tot_alum_promoasis,
            'var_alum_promoasis': self.var_alum_promoasis,
            'tot_discapacidad': self.tot_discapacidad,
            'var_discapacidad': self.var_discapacidad,
            'nom_est': self.nom_est,
            'nro_est': self.nro_est,
            'anio_creac_establec': self.anio_creac_establec,
            'fecha_creac_establec': self.fecha_creac_establec,
            'region': self.region,
            'udt': self.udt,
            'cui': self.cui,
            'cua': self.cua,
            'cuof': self.cuof,
            'sector': self.sector,
            'ambito': self.ambito,
            'ref_loc': self.ref_loc,
            'calle': self.calle,
            'numero': self.numero,
            'localidad': self.localidad,
            'departamento': self.departamento,
            'cod_postal': self.cod_postal,
            'categoria': self.categoria,
            'estado_est': self.estado_est,
            'estado_loc': self.estado_loc,
            'telefono_cod_area': self.telefono_cod_area,
            'telefono_nro': self.telefono_nro,
            'per_funcionamiento': self.per_funcionamiento,
            'email_loc': self.email_loc,
        }