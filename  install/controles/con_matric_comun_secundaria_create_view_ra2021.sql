create
or replace view public.con_matric_comun_secundaria as (
    with naty as (
        select
            *
        from
            consulta_cuadro(158, 'ra_carga2021')
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
        'Común' as tipo_ed,
        'Secundaria' as nivel,
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
                    descripcion as nivel_or
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
            ) as nivel_or USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_12
                from
                    naty
                where
                    id_columna = 98
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as edad_12 USING (cueanexo, id_fila)
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
                    valor :: int as total_rep
                from
                    naty
                where
                    id_columna = 127
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as total_rep USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as var_rep
                from
                    naty
                where
                    id_columna = 128
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as var_rep USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as nro_orden_pe
                from
                    naty
                where
                    id_columna = 165
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as nro_orden_pe USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    descripcion as anio_est
                from
                    naty
                    join codigo_valor as cv on(id_codigo_valor = valor :: int)
                where
                    id_columna = 166
                group by
                    cueanexo,
                    id_fila,
                    descripcion
                order by
                    cueanexo
            ) as anio_est USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor as nom_div
                from
                    naty
                where
                    id_columna = 173
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as nom_div USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    descripcion as tipo_div
                from
                    naty
                    join codigo_valor as cv on (valor :: int = id_codigo_valor)
                where
                    id_columna = 174
                group by
                    cueanexo,
                    id_fila,
                    descripcion
                order by
                    cueanexo
            ) as tipo_div USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    descripcion as orientacion
                from
                    naty
                    join codigo_valor as cv on (valor :: int = id_codigo_valor)
                where
                    id_columna = 175
                group by
                    cueanexo,
                    id_fila,
                    descripcion
                order by
                    cueanexo
            ) as orientacion USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_11_y_menos
                from
                    naty
                where
                    id_columna = 177
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as edad_11_y_menos USING (cueanexo, id_fila)
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
                    valor :: int as edad_25_y_mas
                from
                    naty
                where
                    id_columna = 181
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as edad_25_y_mas USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_20_24
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
            ) as edad_20_24 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor as denom_pe
                from
                    naty
                where
                    id_columna = 551
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as denom_pe USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as total_disc
                from
                    naty
                where
                    id_columna = 870
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as total_disc USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as var_disc
                from
                    naty
                where
                    id_columna = 871
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as var_disc USING (cueanexo, id_fila)
        )
    ORDER BY
        cueanexo,
        id_fila
)