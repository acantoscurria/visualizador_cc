create table rep_matric_especial_inicial as (
       with naty as (
              select
                     *
              from
                     consulta_cuadro(844, 'ra_carga2020')
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
                                   descripcion as sala
                            from
                                   naty
                                   join codigo_valor as b on (id_codigo_valor :: text = valor)
                            where
                                   id_columna = 1
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   descripcion
                            order by
                                   cueanexo
                     ) as sala
                     LEFT JOIN (
                            select
                                   cueanexo,
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
                     ) as turno USING (cueanexo, id_fila)
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
                                   valor as cinco_anios
                            from
                                   naty
                            where
                                   id_columna = 91
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as cinco_anios USING (cueanexo, id_fila)
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
                                   valor as cero_a_dos_anios
                            from
                                   naty
                            where
                                   id_columna = 322
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as cero_a_dos_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as tres_anios
                            from
                                   naty
                            where
                                   id_columna = 481
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as tres_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as cuatro_anios
                            from
                                   naty
                            where
                                   id_columna = 482
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as cuatro_anios USING (cueanexo, id_fila)
                     LEFT JOIN (
                            select
                                   cueanexo,
                                   id_fila,
                                   valor as ocho_o_mas_anios
                            from
                                   naty
                            where
                                   id_columna = 814
                            group by
                                   cueanexo,
                                   escuela,
                                   id_fila,
                                   valor
                            order by
                                   cueanexo
                     ) as ocho_o_mas_anios USING (cueanexo, id_fila)
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