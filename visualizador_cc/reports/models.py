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
        
class RepMatricComunSnu(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cueanexo = models.CharField(max_length=255, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    escuela = models.CharField(max_length=255, blank=True, null=True)
    n_plan_estudio = models.CharField(max_length=255, blank=True, null=True)
    plan_est_titulo = models.CharField(max_length=255, blank=True, null=True)
    tipo_carrera = models.CharField(max_length=255, blank=True, null=True)
    tipo_formacion = models.CharField(max_length=255, blank=True, null=True)
    modalidad_dicatado = models.CharField(max_length=255, blank=True, null=True)
    carrera_termino = models.CharField(max_length=255, blank=True, null=True)
    total = models.CharField(max_length=255, blank=True, null=True)
    total_var = models.CharField(max_length=255, blank=True, null=True)
    menos_18_años = models.CharField(max_length=255, blank=True, null=True)
    edad_18 = models.CharField(max_length=255, blank=True, null=True)
    edad_19 = models.CharField(max_length=255, blank=True, null=True)
    edad_20 = models.CharField(max_length=255, blank=True, null=True)
    edad_21 = models.CharField(max_length=255, blank=True, null=True)
    edad_22 = models.CharField(max_length=255, blank=True, null=True)
    edad_23 = models.CharField(max_length=255, blank=True, null=True)
    edad_24 = models.CharField(max_length=255, blank=True, null=True)
    edad_25 = models.CharField(max_length=255, blank=True, null=True)
    edad_26 = models.CharField(max_length=255, blank=True, null=True)
    edad_27 = models.CharField(max_length=255, blank=True, null=True)
    edad_28 = models.CharField(max_length=255, blank=True, null=True)
    edad_29 = models.CharField(max_length=255, blank=True, null=True)
    edad_30 = models.CharField(max_length=255, blank=True, null=True)
    total_ingresante = models.CharField(max_length=255, blank=True, null=True)
    var_ingresante = models.CharField(max_length=255, blank=True, null=True)
    total_pasantia_practicas = models.CharField(max_length=255, blank=True, null=True)
    var_pasantia_practicas = models.CharField(max_length=255, blank=True, null=True)
    total_residencia = models.CharField(max_length=255, blank=True, null=True)
    var_residencia = models.CharField(max_length=255, blank=True, null=True)
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
        db_table = 'rep_matric_comun_snu'

    def parse (self):
        return{
            'id' : self.id,
            'cueanexo':  self.cueanexo,
            'id_fila': self.id_fila,
            'escuela': self.escuela,
            'n_plan_estudio' : self.n_plan_estudio,
            'plan_est_titulo' : self.plan_est_titulo,
            'tipo_carrera' : self.tipo_carrera,
            'tipo_formacion' : self.tipo_formacion,
            'modalidad_dicatado' : self.modalidad_dicatado,
            'carrera_termino' : self.carrera_termino,
            'total' : self.total,
            'total_var' :self.total_var,
            'menos_18_años' : self.menos_18_años,
            'edad_18': self.edad_18,
            'edad_19': self.edad_19,
            'edad_20': self.edad_20,
            'edad_21': self.edad_21,
            'edad_22': self.edad_22,
            'edad_23': self.edad_23,
            'edad_24': self.edad_24,
            'edad_25': self.edad_25,
            'edad_26': self.edad_26,
            'edad_27': self.edad_27,
            'edad_28': self.edad_28,
            'edad_29': self.edad_29,
            'edad_30': self.edad_30,
            'total_ingresante' : self.total_ingresante,
            'var_ingresante' : self.var_ingresante,
            'total_pasantia_practicas' : self.total_pasantia_practicas,
            'var_pasantia_practicas' : self.var_pasantia_practicas,
            'total_residencia' : self.total_residencia,
            'var_residencia' : self.var_residencia,
            'nom_est': self.nom_est,
            'nro_est': self.nro_est,
            'anio_creac_establec' : self.anio_creac_establec,
            'fecha_creac_establec' : self.fecha_creac_establec,
            'region' : self.region,
            'udt' : self.udt,
            'cui' : self.cui,
            'cua' : self.cua,
            'cuof' : self.cuof,
            'sector' : self.sector,
            'ambito' : self.ambito,
            'ref_loc': self.ref_loc,
            'call' : self.calle,
            'numero' : self.numero,
            'localidad' :self.localidad,
            'departamento' : self.departamento,
            'cod_postal' : self.cod_postal,
            'categoria' :self.categoria,
            'estado_est' : self.estado_est,
            'estado_loc' : self.estado_loc,
            'telefono_cod_area' : self.telefono_cod_area,
            'telefono_nro' : self.telefono_nro,
            'per_funcionamiento' : self.per_funcionamiento,
            'email_loc' :self.email_loc,
        }
        
class RepMatricAdultosPrimaria(models.Model):
    id = models.BigIntegerField(primary_key=True)
    cueanexo = models.CharField(max_length=255, blank=True, null=True)
    id_fila = models.IntegerField(blank=True, null=True)
    turno = models.CharField(max_length=255, blank=True, null=True)
    tipo_secc = models.CharField(max_length=255, blank=True, null=True)
    nivel = models.CharField(max_length=255, blank=True, null=True)
    nom_secc = models.CharField(max_length=255, blank=True, null=True)
    ciclo_etapa = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    total_var = models.IntegerField(blank=True, null=True)
    edad_menos_13 = models.IntegerField(blank=True, null=True)
    edad_13 = models.IntegerField(blank=True, null=True)
    edad_14 = models.IntegerField(blank=True, null=True)
    edad_15 = models.IntegerField(blank=True, null=True)
    edad_16 = models.IntegerField(blank=True, null=True)
    edad_17 = models.IntegerField(blank=True, null=True)
    edad_18 = models.IntegerField(blank=True, null=True)
    edad_19 = models.IntegerField(blank=True, null=True)
    edad_20_a_24 = models.IntegerField(blank=True, null=True)
    edad_25_a_29 = models.IntegerField(blank=True, null=True)
    edad_30_a_34 = models.IntegerField(blank=True, null=True)
    edad_35_a_39 = models.IntegerField(blank=True, null=True)
    edad_40_a_44 = models.IntegerField(blank=True, null=True)
    edad_45_a_49 = models.IntegerField(blank=True, null=True)
    edad_50_a_54 = models.IntegerField(blank=True, null=True)
    edad_55_y_mas = models.IntegerField(blank=True, null=True)
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
        db_table = 'rep_matric_adultos_primaria'

    def parse (self):
        return{
            'id': self.id,
            'cueanexo': self.cueanexo,
            'id_fila': self.id_fila,
            'turno': self.turno,
            'tipo_secc': self.tipo_secc,
            'nivel': self.nivel,
            'nom_secc': self.nom_secc,
            'ciclo_etapa': self.ciclo_etapa,
            'total': self.total,
            'total_var': self.total_var,
            'edad_menos_13': self.edad_menos_13,
            'edad_13': self.edad_13,
            'edad_14': self.edad_14,
            'edad_15': self.edad_15,
            'edad_16': self.edad_16,
            'edad_17': self.edad_17,
            'edad_18': self.edad_18,
            'edad_19': self.edad_19,
            'edad_20_a_24': self.edad_20_a_24,
            'edad_25_a_29': self.edad_25_a_29,
            'edad_30_a_34': self.edad_30_a_34,
            'edad_35_a_39': self.edad_35_a_39,
            'edad_40_a_44': self.edad_40_a_44,
            'edad_45_a_49': self.edad_45_a_49,
            'edad_50_a_54': self.edad_50_a_54,
            'edad_55_y_mas': self.edad_55_y_mas,
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