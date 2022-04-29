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
    menos_1_anio = models.IntegerField(blank=True, null=True)
    un_anio = models.IntegerField(blank=True, null=True)
    dos_anios = models.IntegerField(blank=True, null=True)
    tres_anios = models.IntegerField(blank=True, null=True)
    cuatro_anios = models.IntegerField(blank=True, null=True)
    cinco_anios = models.IntegerField(blank=True, null=True)
    seis_anios = models.IntegerField(blank=True, null=True)
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
        db_table = 'rep_matric_comun_inicial'

 
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
            "menos_1_anio": self.menos_1_anio,
            "un_anio": self.un_anio,
            "dos_anios": self.dos_anios,
            "tres_anios": self.tres_anios,
            "cuatro_anios": self.cuatro_anios,
            "cinco_anios": self.cinco_anios,
            "seis_anios": self.seis_anios,
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
          
class RepMatricComunPrimaria(models.Model):
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
        db_table = 'rep_matric_comun_primaria'

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
            'grado_anio': self.grado_anio,
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
        
class RepMatricComunSecundaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cueanexo = models.CharField(max_length=255, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    total_var = models.IntegerField(blank=True, null=True)
    nivel = models.CharField(max_length=255, blank=True, null=True)
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
        db_table = 'rep_matric_comun_secundaria'

    def parse (self):
        return {
            'id': self.id,
            'cueanexo': self.cueanexo,
            'id_fila': self.id_fila,
            'turno': self.turno,
            'total': self.total,
            'total_var': self.total_var,
            'nivel': self.nivel,
            'edad_12': self.edad_12,
            'edad_13': self.edad_13,
            'edad_14': self.edad_14,
            'edad_15': self.edad_15,
            'edad_16': self.edad_16,
            'edad_17': self.edad_17,
            'total_rep': self.total_rep,
            'var_rep': self.var_rep,
            'nro_orden_pe': self.nro_orden_pe,
            'anio_est': self.anio_est,
            'nom_div': self.nom_div,
            'tipo_div': self.tipo_div,
            'orientacion': self.orientacion,
            'edad_11_y_menos': self.edad_11_y_menos,
            'edad_18': self.edad_18,
            'edad_19': self.edad_19,
            'edad_25_y_mas': self.edad_25_y_mas,
            'edad_20_24': self.edad_20_24,
            'denom_pe': self.denom_pe,
            'total_disc': self.total_disc,
            'var_disc': self.var_disc,
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