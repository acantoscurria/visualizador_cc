create table rep_matric_adultos_primaria as (
with naty as (
       select
              *
       from
              consulta_cuadro(297, 'ra_carga2021')
),
codigo_valor as (
       select
              *
       from
              dblink (
                     'dbname=ra_carga2021 user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' :: text,
                     'select id_codigo_valor, descripcion
										  from codigo_valor' :: text
              ) as codigo_valor (id_codigo_valor int, descripcion varchar)
)
select
       row_number() over () as id,	
       *
from
       (
              (
                     select
                            cueanexo,
                            escuela,
                            id_fila,
                            descripcion as turno
                     from
                            naty
                            join codigo_valor as cv on (id_codigo_valor = valor :: int)
                     where
                            id_columna = 2
                     group by
                            cueanexo,
                            escuela,
                            id_fila,
                            descripcion
                     order by
                            cueanexo
              ) as turno
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            descripcion as tipo_secc
                     from
                            naty
                            join codigo_valor as cv on (valor :: int = id_codigo_valor)
                     where
                            id_columna = 4
                     group by
                            cueanexo,
                            id_fila,
                            descripcion
                     order by
                            cueanexo
              ) as tipo_secc USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            descripcion as nivel 
                     from
                            naty
                            join codigo_valor as cv on (valor :: int = id_codigo_valor)
                     where
                            id_columna = 55
                     group by
                            cueanexo,
                            id_fila,
                            descripcion
                     order by
                            cueanexo
              ) as nivel  USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor as nom_secc
                     from
                            naty
                     where
                            id_columna = 90
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as nom_sec USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            descripcion as ciclo_etapa
                     from
                            naty
                            join codigo_valor as cv on (id_codigo_valor = valor :: int)
                     where
                            id_columna = 398
                     group by
                            cueanexo,
                            id_fila,
                            descripcion
                     order by
                            cueanexo
              ) as ciclo_etapa USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as total
                     from
                            naty
                     where
                            id_columna = 5
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as total USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as total_var
                     from
                            naty
                     where
                            id_columna = 7
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as varones USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_menos_13
                     from
                            naty
                     where
                            id_columna = 421
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_menos_13 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_13
                     from
                            naty
                     where
                            id_columna = 99
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_13 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_14
                     from
                            naty
                     where
                            id_columna = 100
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_14 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_15
                     from
                            naty
                     where
                            id_columna = 101
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_15 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_16
                     from
                            naty
                     where
                            id_columna = 102
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_16 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_17
                     from
                            naty
                     where
                            id_columna = 103
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_17 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_18
                     from
                            naty
                     where
                            id_columna = 178
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_18 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_19
                     from
                            naty
                     where
                            id_columna = 179
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_19 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_20_a_24
                     from
                            naty
                     where
                            id_columna = 301
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_20_a_24 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_25_a_29
                     from
                            naty
                     where
                            id_columna = 302
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_25_a_29 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_30_a_34
                     from
                            naty
                     where
                            id_columna = 303
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_30_a_34 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_35_a_39
                     from
                            naty
                     where
                            id_columna = 304
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_35_a_39 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_40_a_44
                     from
                            naty
                     where
                            id_columna = 334
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_40_a_44 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_45_a_49
                     from
                            naty
                     where
                            id_columna = 335
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_45_a_49 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_50_a_54
                     from
                            naty
                     where
                            id_columna = 394
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_50_a_54 USING (cueanexo, id_fila)
              LEFT JOIN (
                     select
                            cueanexo,
                            id_fila,
                            valor :: int as edad_55_y_mas
                     from
                            naty
                     where
                            id_columna = 395
                     group by
                            cueanexo,
                            id_fila,
                            valor
                     order by
                            cueanexo
              ) as edad_55_y_mas USING (cueanexo, id_fila)
       )
       LEFT JOIN (
              select
                     *
              from
                     dblink (
                            'dbname=padron user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' :: text,
                            'select distinct cueanexo,nom_est,nro_est,anio_creac_establec,fecha_creac_establec,region,udt,cui,
cua,cuof,sector,ambito,ref_loc,calle,numero,localidad,departamento,cod_postal,categoria,estado_est,
estado_loc,telefono_cod_area,telefono_nro,per_funcionamiento,email_loc from padron' :: text
                     ) as padron (
                            cueanexo varchar,
                            nom_est varchar,
                            nro_est varchar,
                            anio_creac_establec varchar,
                            fecha_creac_establec varchar,
                            region varchar,
                            udt varchar,
                            cui varchar,
                            cua varchar,
                            cuof varchar,
                            sector varchar,
                            ambito varchar,
                            ref_loc varchar,
                            calle varchar,
                            numero varchar,
                            localidad varchar,
                            departamento varchar,
                            cod_postal varchar,
                            categoria varchar,
                            estado_est varchar,
                            estado_loc varchar,
                            telefono_cod_area varchar,
                            telefono_nro varchar,
                            per_funcionamiento varchar,
                            email_loc varchar
                     )
       ) AS p using (cueanexo)
order by
       cueanexo,
       id_fila 
)