var eb = function(c){
    let s = ""
    for (let i = 0; i < c; i++) {
        s+="&nbsp"             
    }
    return s
}

var columns = {
    none: {
        none: [{}]
    },
    'ra2021': {
        none: [{}],
        matricula_comun_inicial: [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "#",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_ed",
                "name": "tipo_ed",
                "title": "Tipo ed.",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nivel",
                "name": "nivel",
                "title": "Nivel",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "Cueanexo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "id_fila",
                "name": "id_fila",
                "title": "Id fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "escuela",
                "name": "escuela",
                "title": eb(25)+"Escuela"+eb(25),
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "sala",
                "name": "sala",
                "title": "Sala",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "turno",
                "name": "turno",
                "title": "Turno",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_secc",
                "name": "nom_secc",
                "title": "Nom secc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_secc",
                "name": "tipo_secc",
                "title": "Tipo secc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total",
                "name": "total",
                "title": "Total",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_var",
                "name": "total_var",
                "title": "Total var",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "menos_1_anio",
                "name": "menos_1_anio",
                "title": "Menos 1 anio",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "un_anio",
                "name": "un_anio",
                "title": "Un anio",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "dos_anios",
                "name": "dos_anios",
                "title": "Dos anios",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tres_anios",
                "name": "tres_anios",
                "title": "Tres anios",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cuatro_anios",
                "name": "cuatro_anios",
                "title": "Cuatro anios",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cinco_anios",
                "name": "cinco_anios",
                "title": "Cinco anios",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "seis_anios",
                "name": "seis_anios",
                "title": "Seis anios",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_disc",
                "name": "total_disc",
                "title": "Total disc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            
        ],
        
        matricula_comun_primaria: [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "#",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "Cueanexo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "id_fila",
                "name": "id_fila",
                "title": "Id fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "escuela",
                "name": "escuela",
                "title": eb(25)+"Escuela"+eb(25),
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "turno",
                "name": "turno",
                "title": "Turno",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nombre_secc",
                "name": "nombre_secc",
                "title": "Nombre Sec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_secc",
                "name": "tipo_secc",
                "title": "Tipo Sec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total",
                "name": "total",
                "title": "Total",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_var",
                "name": "total_var",
                "title": "Total Var",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nivel",
                "name": "nivel",
                "title": "Nivel",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "grado_anio",
                "name": "grado_anio",
                "title": "Grado anio",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_5",
                "name": "edad_5",
                "title": "Edad 5",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_6",
                "name": "edad_6",
                "title": "Edad 6",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_7",
                "name": "edad_7",
                "title": "Edad 7",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_8",
                "name": "edad_8",
                "title": "Edad 8",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_9",
                "name": "edad_9",
                "title": "Edad 9",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_10",
                "name": "edad_10",
                "title": "Edad 10",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_11",
                "name": "edad_11",
                "title": "Edad 11",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_12",
                "name": "edad_12",
                "title": "Edad 12",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_13",
                "name": "edad_13",
                "title": "Edad 13",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_14",
                "name": "edad_14",
                "title": "Edad 14",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_15",
                "name": "edad_15",
                "title": "Edad 15",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_16",
                "name": "edad_16",
                "title": "Edad 16",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_18_y_mas",
                "name": "edad_18_y_mas",
                "title": "Edad 18 y Más",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_rep",
                "name": "total_rep",
                "title": "Total Repitentes",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_rep",
                "name": "var_rep",
                "title": "Varones Repitentes",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tot_alum_promoasis",
                "name": "tot_alum_promoasis",
                "title": "tot_alum_promoasis",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tot_discapacidad",
                "name": "tot_discapacidad",
                "title": "tot_discapacidad",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_discapacidad",
                "name": "var_discapacidad",
                "title": "var_discapacidad",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_est",
                "name": "nom_est",
                "title": "nom_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "anio_creac_establec",
                "name": "anio_creac_establec",
                "title": "anio_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "fecha_creac_establec",
                "name": "fecha_creac_establec",
                "title": "fecha_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "region",
                "name": "region",
                "title": "region",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "udt",
                "name": "udt",
                "title": "tot_alum_promoasis",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cui",
                "name": "cui",
                "title": "cui",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cua",
                "name": "cua",
                "title": "cua",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cuof",
                "name": "cuof",
                "title": "cuof",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "sector",
                "name": "sector",
                "title": "sector",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ambito",
                "name": "ambito",
                "title": "ambito",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ref_loc",
                "name": "ref_loc",
                "title": "ref_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "calle",
                "name": "calle",
                "title": "calle",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "numero",
                "name": "numero",
                "title": "numero",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "localidad",
                "name": "localidad",
                "title": "localidad",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "departamento",
                "name": "departamento",
                "title": "departamento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cod_postal",
                "name": "cod_postal",
                "title": "cod_postal",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "categoria",
                "name": "categoria",
                "title": "categoria",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_est",
                "name": "estado_est",
                "title": "estado_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_loc",
                "name": "estado_loc",
                "title": "estado_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_cod_area",
                "name": "telefono_cod_area",
                "title": "telefono_cod_area",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_nro",
                "name": "telefono_nro",
                "title": "telefono_nro",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "per_funcionamiento",
                "name": "per_funcionamiento",
                "title": "per_funcionamiento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "email_loc",
                "name": "email_loc",
                "title": "email_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
        ],
        matricula_comun_secundaria: [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "#",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "Cueanexo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "id_fila",
                "name": "id_fila",
                "title": "id_fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "turno",
                "name": "turno",
                "title": "turno",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total",
                "name": "total",
                "title": "total",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_var",
                "name": "total_var",
                "title": "total_var",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nivel",
                "name": "nivel",
                "title": "nivel",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_12",
                "name": "edad_12",
                "title": "edad_12",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_13",
                "name": "edad_13",
                "title": "edad_13",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_14",
                "name": "edad_14",
                "title": "edad_14",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_15",
                "name": "edad_15",
                "title": "edad_15",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_16",
                "name": "edad_16",
                "title": "edad_16",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_17",
                "name": "edad_17",
                "title": "edad_17",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_11_y_menos",
                "name": "edad_11_y_menos",
                "title": "edad_11_y_menos",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_18",
                "name": "edad_18",
                "title": "edad_18",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_19",
                "name": "edad_19",
                "title": "edad_19",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_20_24",
                "name": "edad_20_24",
                "title": "edad_20_24",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_25_y_mas",
                "name": "edad_25_y_mas",
                "title": "edad_25_y_mas",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_rep",
                "name": "total_rep",
                "title": "total_rep",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_rep",
                "name": "var_rep",
                "title": "var_rep",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nro_orden_pe",
                "name": "nro_orden_pe",
                "title": "nro_orden_pe",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "anio_est",
                "name": "anio_est",
                "title": "anio_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_div",
                "name": "nom_div",
                "title": "nom_div",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_div",
                "name": "tipo_div",
                "title": "tipo_div",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "orientacion",
                "name": "orientacion",
                "title": "orientacion",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "denom_pe",
                "name": "denom_pe",
                "title": "denom_pe",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_disc",
                "name": "total_disc",
                "title": "total_disc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_est",
                "name": "nom_est",
                "title": "nom_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nro_Est",
                "name": "nro_Est",
                "title": "nro_Est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "anio_creac_establec",
                "name": "anio_creac_establec",
                "title": "anio_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "fecha_creac_establec",
                "name": "fecha_creac_establec",
                "title": "fecha_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "region",
                "name": "region",
                "title": "region",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "udt",
                "name": "udt",
                "title": "udt",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cui",
                "name": "cui",
                "title": "cui",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cua",
                "name": "cua",
                "title": "cua",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cuof",
                "name": "cuof",
                "title": "cuof",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "sector",
                "name": "sector",
                "title": "sector",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ambito",
                "name": "ambito",
                "title": "ambito",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ref_loc",
                "name": "ref_loc",
                "title": "ref_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "calle",
                "name": "calle",
                "title": "calle",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "numero",
                "name": "numero",
                "title": "numero",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "localidad",
                "name": "localidad",
                "title": "localidad",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "departamento",
                "name": "departamento",
                "title": "departamento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cod_postal",
                "name": "cod_postal",
                "title": "cod_postal",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "categoria",
                "name": "categoria",
                "title": "categoria",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_est",
                "name": "estado_est",
                "title": "estado_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_loc",
                "name": "estado_loc",
                "title": "estado_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_cod_area",
                "name": "telefono_cod_area",
                "title": "telefono_cod_area",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_nro",
                "name": "telefono_nro",
                "title": "telefono_nro",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "per_funcionamiento",
                "name": "per_funcionamiento",
                "title": "per_funcionamiento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "email_loc",
                "name": "email_loc",
                "title": "email_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },

        ],
        matricula_comun_snu: [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "id",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "cueanexo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "id_fila",
                "name": "id_fila",
                "title": "id_fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "escuela",
                "name": "escuela",
                "title": "escuela",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "n_plan_estudio",
                "name": "n_plan_estudio",
                "title": "n_plan_estudio",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "plan_est_titulo",
                "name": "plan_est_titulo",
                "title": "plan_est_titulo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_carrera",
                "name": "tipo_carrera",
                "title": "tipo_carrera",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_formacion",
                "name": "tipo_formacion",
                "title": "tipo_formacion",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "modalidad_dicatado",
                "name": "modalidad_dicatado",
                "title": "modalidad_dicatado",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "carrera_termino",
                "name": "carrera_termino",
                "title": "carrera_termino",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total",
                "name": "total",
                "title": "total",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_var",
                "name": "total_var",
                "title": "total_var",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "menos_18_años",
                "name": "menos_18_años",
                "title": "menos_18_años",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_18",
                "name": "edad_18",
                "title": "edad_18",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_19",
                "name": "edad_19",
                "title": "edad_19",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_20",
                "name": "edad_20",
                "title": "edad_20",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_21",
                "name": "edad_21",
                "title": "edad_21",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_22",
                "name": "edad_22",
                "title": "edad_22",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_23",
                "name": "edad_23",
                "title": "edad_23",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_24",
                "name": "edad_24",
                "title": "edad_24",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_25",
                "name": "edad_25",
                "title": "edad_25",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_26",
                "name": "edad_26",
                "title": "edad_26",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_27",
                "name": "edad_27",
                "title": "edad_27",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_28",
                "name": "edad_28",
                "title": "edad_28",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_29",
                "name": "edad_29",
                "title": "edad_29",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_30",
                "name": "edad_30",
                "title": "edad_30",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_ingresante",
                "name": "total_ingresante",
                "title": "total_ingresante",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_ingresante",
                "name": "var_ingresante",
                "title": "var_ingresante",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_pasantia_practicas",
                "name": "total_pasantia_practicas",
                "title": "total_pasantia_practicas",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_pasantia_practicas",
                "name": "var_pasantia_practicas",
                "title": "var_pasantia_practicas",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_residencia",
                "name": "total_residencia",
                "title": "total_residencia",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "var_residencia",
                "name": "var_residencia",
                "title": "var_residencia",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_est",
                "name": "nom_est",
                "title": "nom_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nro_est",
                "name": "nro_est",
                "title": "nro_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "anio_creac_establec",
                "name": "anio_creac_establec",
                "title": "anio_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "fecha_creac_establec",
                "name": "fecha_creac_establec",
                "title": "fecha_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "region",
                "name": "region",
                "title": "region",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "dt",
                "name": "dt",
                "title": "dt",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ui",
                "name": "ui",
                "title": "ui",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ua",
                "name": "ua",
                "title": "ua",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cuf",
                "name": "cuf",
                "title": "cuf",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "sector",
                "name": "sector",
                "title": "sector",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ambito",
                "name": "ambito",
                "title": "ambito",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ref_loc",
                "name": "ref_loc",
                "title": "ref_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "call",
                "name": "call",
                "title": "call",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "numero",
                "name": "numero",
                "title": "numero",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "localidad",
                "name": "localidad",
                "title": "localidad",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "departamento",
                "name": "departamento",
                "title": "departamento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cod_postal",
                "name": "cod_postal",
                "title": "cod_postal",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "categoria",
                "name": "categoria",
                "title": "categoria",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_est",
                "name": "estado_est",
                "title": "estado_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_loc",
                "name": "estado_loc",
                "title": "estado_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_cod_area",
                "name": "telefono_cod_area",
                "title": "telefono_cod_area",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_nro",
                "name": "telefono_nro",
                "title": "telefono_nro",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "per_funcionamiento",
                "name": "per_funcionamiento",
                "title": "per_funcionamiento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "email_loc",
                "name": "email_loc",
                "title": "email_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },

        ],
        matricula_adultos_primaria: [
            {
                "class": "left row-control",
                "data": "id",
                "name": "id",
                "title": "id",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cueanexo",
                "name": "cueanexo",
                "title": "cueanexo",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "id_fila",
                "name": "id_fila",
                "title": "id_fila",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "turno",
                "name": "turno",
                "title": "turno",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "tipo_secc",
                "name": "tipo_secc",
                "title": "tipo_secc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nivel",
                "name": "nivel",
                "title": "nivel",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_secc",
                "name": "nom_secc",
                "title": "nom_secc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ciclo_etapa",
                "name": "ciclo_etapa",
                "title": "ciclo_etapa",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total",
                "name": "total",
                "title": "total",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "total_var",
                "name": "total_var",
                "title": "total_var",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_menos_13",
                "name": "edad_menos_13",
                "title": "edad_menos_13",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_13",
                "name": "edad_13",
                "title": "edad_13",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_14",
                "name": "edad_14",
                "title": "edad_14",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_15",
                "name": "edad_15",
                "title": "edad_15",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_16",
                "name": "edad_16",
                "title": "edad_16",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_17",
                "name": "edad_17",
                "title": "edad_17",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_18",
                "name": "edad_18",
                "title": "edad_18",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_19",
                "name": "edad_19",
                "title": "edad_19",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_20_a_24",
                "name": "edad_20_a_24",
                "title": "edad_20_a_24",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_25_a_29",
                "name": "edad_25_a_29",
                "title": "edad_25_a_29",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_30_a_34",
                "name": "edad_30_a_34",
                "title": "edad_30_a_34",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_35_a_39",
                "name": "edad_35_a_39",
                "title": "edad_35_a_39",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_40_a_44",
                "name": "edad_40_a_44",
                "title": "edad_40_a_44",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_45_a_49",
                "name": "edad_45_a_49",
                "title": "edad_45_a_49",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_50_a_54",
                "name": "edad_50_a_54",
                "title": "edad_50_a_54",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "edad_55_y_mas",
                "name": "edad_55_y_mas",
                "title": "edad_55_y_mas",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nom_est",
                "name": "nom_est",
                "title": "nom_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "nro_est",
                "name": "nro_est",
                "title": "nro_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "anio_creac_establec",
                "name": "anio_creac_establec",
                "title": "anio_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "fecha_creac_establec",
                "name": "fecha_creac_establec",
                "title": "fecha_creac_establec",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "region",
                "name": "region",
                "title": "region",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "udt",
                "name": "udt",
                "title": "udt",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cui",
                "name": "cui",
                "title": "cui",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cua",
                "name": "cua",
                "title": "cua",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cuof",
                "name": "cuof",
                "title": "cuof",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "sector",
                "name": "sector",
                "title": "sector",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ambito",
                "name": "ambito",
                "title": "ambito",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "ref_loc",
                "name": "ref_loc",
                "title": "ref_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "calle",
                "name": "calle",
                "title": "calle",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "numero",
                "name": "numero",
                "title": "numero",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "localidad",
                "name": "localidad",
                "title": "localidad",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "departamento",
                "name": "departamento",
                "title": "departamento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "cod_postal",
                "name": "cod_postal",
                "title": "cod_postal",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "categoria",
                "name": "categoria",
                "title": "categoria",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_est",
                "name": "estado_est",
                "title": "estado_est",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "estado_loc",
                "name": "estado_loc",
                "title": "estado_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_cod_area",
                "name": "telefono_cod_area",
                "title": "telefono_cod_area",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "telefono_nro",
                "name": "telefono_nro",
                "title": "telefono_nro",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "per_funcionamiento",
                "name": "per_funcionamiento",
                "title": "per_funcionamiento",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
            {
                "class": "left row-control",
                "data": "email_loc",
                "name": "email_loc",
                "title": "email_loc",
                "render": function ( data, type, row ) {
                    return data ? data : ''
                }
            },
        ]
    },
}

$(document).ready(function(){

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    var dt_matricula = null

    var reloadInstanceDatatable = function(){

        if($("#matricula_input").val() == "none" || $("#relevamiento_input").val() == "none"){

            $(".alert-msg-none-selection").show()
        }
        else{

            $(".alert-msg-none-selection").hide()

            if(dt_matricula){

                dt_matricula.clear();
                dt_matricula.destroy();

                $("#tabla-matricula tbody").empty();
                $("#tabla-matricula thead").empty();
            }    

            console.log("columns", columns[$("#relevamiento_input").val()][$("#matricula_input").val()])     

            dt_matricula = $("#tabla-matricula")
            .on( 'processing.dt', function ( e, settings, processing ) {
                if (processing) {
                } 
            })
            .DataTable({
                "ajax": {
                    "url": "/reports/ra_matricula_list/",
                    "type": "POST",
                    "headers": {'X-CSRFToken': csrftoken },
                    "dataFilter": function( data ) {
                        if (data) {
                            try {
                                let json = $.parseJSON( data )
                                if(json.error_msg){
                                    alert(json.error_msg)
                                }  
                                return data                
    
                            } catch(e) {
                                console.error('error al obtener los datos de la tabla', e);
                            }
                        }
                    },
                    "data": function ( d ) {
                        return $.extend( {}, d, {
                            "matricula_selected": $("#matricula_input").val(),
                            "ra_selected": $("#relevamiento_input").val(),
                        })
                    },
    
                },
                "columns": columns[$("#relevamiento_input").val()][$("#matricula_input").val()],     
                "processing":true,
                "serverSide": true,
                "autoWidth": true,
                "orderCellsTop": false,
                //"order": [[ 1, 'asc' ]],
                //"rowId": 'id',
                "scrollY": true,
                "scrollY": '600px',
                "scrollX": true,
                "scrollCollapse": true,
                "paging": true,
                "ordering": false,
                "createdRow": function( row, data, index ) {
    
                },
                "infoCallback": function( settings, start, end, max, total, pre ) {
    
                    return pre
                },
                "initComplete": function(settings, json) {
    
                    console.log( 'DataTables has finished its initialisation.' );          
            
                },
                "language": {
                    decimal: "",
                    emptyTable: "Sin resultados.",
                    info: "_START_ al _END_ de _TOTAL_",
                    infoEmpty: "0 al 0 de 0",
                    infoFiltered: "",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar _MENU_ filas",
                    loadingRecords: $('#preloader').html(),
                    processing: $('#preloader').html(),
                    search: "Buscar:",
                    zeroRecords: "Sin resultados",
                    paginate: {
                        first: "Primero",
                        last: "Último",
                        next: "Siguiente",
                        previous: "Anterior"
                    },
                    aria: {
                        sortAscending: ": Activar para ordenar la columna ascendente",
                        sortDescending: ": Activar para ordenar la columna descendente"
                    }
                },
                "pagingType": "numbers",
                "lengthMenu": [[10, 100, 500, 1000, -1], [10, 100, 500, 1000, "Todas"]],
                "dom": 'frtip',
                "buttons": [
                        'copy', 'csv', 'excel', 'pdf', 'print'
                    ]
                
            }) 

        }


       
        
    }

    $("#matricula_input").change(function(){

        reloadInstanceDatatable()
    })

    $("#relevamiento_input").change(function(){

        reloadInstanceDatatable()
    })

    reloadInstanceDatatable()

})