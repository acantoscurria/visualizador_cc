create table rep_matric_especial_primaria as (
       with naty as (
              select
                     *
              from
                     consulta_cuadro(514, 'ra_carga2020')
       ),
       codigo_valor as (
              select
                     *
              from
                     dblink (
                            'dbname=ra_carga2020 user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' :: text,
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
                                   join codigo_valor as b on (id_codigo_valor :: text = valor)
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
                                   join codigo_valor as b on (id_codigo_valor :: text = valor)
                            where
                                   id_columna = 4
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   descripcion
                            order by
                                   cueanexo
                     ) as tipo_secc USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as total
                            from
                                   naty
                            where
                                   id_columna = 5
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as total USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as total_var
                            from
                                   naty
                            where
                                   id_columna = 7
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as total_var USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   descripcion as grado_anio
                            from
                                   naty
                                   join codigo_valor as b on (id_codigo_valor :: text = valor)
                            where
                                   id_columna = 89
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   descripcion
                            order by
                                   cueanexo
                     ) as grado_anio USING (cueanexo, id_fila)
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
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as nom_secc USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as seis_anios
                            from
                                   naty
                            where
                                   id_columna = 92
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as seis_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as siete_anios
                            from
                                   naty
                            where
                                   id_columna = 93
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as siete_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as ocho_anios
                            from
                                   naty
                            where
                                   id_columna = 94
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as ocho_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as nueve_anios
                            from
                                   naty
                            where
                                   id_columna = 95
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as nueve_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as diez_anios
                            from
                                   naty
                            where
                                   id_columna = 96
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as diez_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as once_anios
                            from
                                   naty
                            where
                                   id_columna = 97
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as once_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as doce_anios
                            from
                                   naty
                            where
                                   id_columna = 98
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as doce_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as trece_anios
                            from
                                   naty
                            where
                                   id_columna = 99
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as trece_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as catorce_anios
                            from
                                   naty
                            where
                                   id_columna = 100
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as catorce_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as quince_anios
                            from
                                   naty
                            where
                                   id_columna = 101
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as quince_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as dieciseis_anios
                            from
                                   naty
                            where
                                   id_columna = 102
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as dieciseis_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as diecisiete_anios
                            from
                                   naty
                            where
                                   id_columna = 103
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as diecisiete_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as dieciocho_anios
                            from
                                   naty
                            where
                                   id_columna = 178
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as dieciocho_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as total_rep
                            from
                                   naty
                            where
                                   id_columna = 127
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as total_rep USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as var_rep
                            from
                                   naty
                            where
                                   id_columna = 128
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as var_rep USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as diecinueve_mas
                            from
                                   naty
                            where
                                   id_columna = 486
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as diecinueve_mas USING (cueanexo, id_fila)
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