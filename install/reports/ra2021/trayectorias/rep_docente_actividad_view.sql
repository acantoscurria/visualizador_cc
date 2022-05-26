create view rep_docente_actividad as(
    WITH naty AS (
        SELECT
            consulta_cuadro.cueanexo,
            consulta_cuadro.escuela,
            consulta_cuadro.id_definicion_cuadro,
            consulta_cuadro.id_fila,
            consulta_cuadro.fila,
            consulta_cuadro.id_columna,
            consulta_cuadro.columna,
            consulta_cuadro.valor
        FROM
            consulta_cuadro(550, 'ra_carga2021' :: character varying) consulta_cuadro(
                cueanexo,
                escuela,
                id_definicion_cuadro,
                id_fila,
                fila,
                id_columna,
                columna,
                valor
            )
    )
    SELECT
        row_number() OVER () AS id,
        'Especial' :: text AS tipo_ed,
        'Todos los Niveles' :: text AS nivel,
        total.cueanexo,
        total.id_fila,
        total.escuela,
        total.nivel1,
        total.total,
        varones.varones,
        p.nom_est,
        p.nro_est,
        p.anio_creac_establec,
        p.fecha_creac_establec,
        p.region,
        p.udt,
        p.cui,
        p.cua,
        p.cuof,
        p.sector,
        p.ambito,
        p.ref_loc,
        p.calle,
        p.numero,
        p.localidad,
        p.departamento,
        p.cod_postal,
        p.categoria,
        p.estado_est,
        p.estado_loc,
        p.telefono_cod_area,
        p.telefono_nro,
        p.per_funcionamiento,
        p.email_loc
    FROM
        (
            SELECT
                naty.cueanexo,
                naty.escuela,
                naty.id_fila,
                naty.fila AS nivel1,
                naty.valor AS total
            FROM
                naty
            WHERE
                naty.id_columna = 5
            GROUP BY
                naty.cueanexo,
                naty.escuela,
                naty.id_fila,
                naty.fila,
                naty.valor
            ORDER BY
                naty.cueanexo
        ) total
        LEFT JOIN (
            SELECT
                naty.cueanexo,
                naty.id_fila,
                naty.valor AS varones
            FROM
                naty
            WHERE
                naty.id_columna = 7
            GROUP BY
                naty.cueanexo,
                naty.escuela,
                naty.id_fila,
                naty.valor
            ORDER BY
                naty.cueanexo
        ) varones USING (cueanexo, id_fila)
        LEFT JOIN (
            SELECT
                padron.cueanexo,
                padron.nom_est,
                padron.nro_est,
                padron.anio_creac_establec,
                padron.fecha_creac_establec,
                padron.region,
                padron.udt,
                padron.cui,
                padron.cua,
                padron.cuof,
                padron.sector,
                padron.ambito,
                padron.ref_loc,
                padron.calle,
                padron.numero,
                padron.localidad,
                padron.departamento,
                padron.cod_postal,
                padron.categoria,
                padron.estado_est,
                padron.estado_loc,
                padron.telefono_cod_area,
                padron.telefono_nro,
                padron.per_funcionamiento,
                padron.email_loc
            FROM
                dblink(
                    'dbname=padron user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' :: text,
                    'select distinct cueanexo,nom_est,nro_est,anio_creac_establec,fecha_creac_establec,region,udt,cui,
cua,cuof,sector,ambito,ref_loc,calle,numero,localidad,departamento,cod_postal,categoria,estado_est,
estado_loc,telefono_cod_area,telefono_nro,per_funcionamiento,email_loc from padron' :: text
                ) padron(
                    cueanexo character varying,
                    nom_est character varying,
                    nro_est character varying,
                    anio_creac_establec character varying,
                    fecha_creac_establec character varying,
                    region character varying,
                    udt character varying,
                    cui character varying,
                    cua character varying,
                    cuof character varying,
                    sector character varying,
                    ambito character varying,
                    ref_loc character varying,
                    calle character varying,
                    numero character varying,
                    localidad character varying,
                    departamento character varying,
                    cod_postal character varying,
                    categoria character varying,
                    estado_est character varying,
                    estado_loc character varying,
                    telefono_cod_area character varying,
                    telefono_nro character varying,
                    per_funcionamiento character varying,
                    email_loc character varying
                )
        ) p USING (cueanexo)
    ORDER BY
        total.cueanexo,
        total.id_fila

)