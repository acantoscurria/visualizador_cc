create view public.con_matric_comun_primaria as (
    with naty as (
        select
            *
        from
            consulta_cuadro(626, 'ra_carga2021')
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
        'Primaria' as nivel,
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
                    valor as nombre_secc
                from
                    naty
                where
                    id_columna = 3
                group by
                    cueanexo,
                    escuela,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as nombre_secc USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    descripcion as tipo_secc
                from
                    naty
                    join codigo_valor as c on (id_codigo_valor :: text = valor)
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
                    valor :: int as total
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
                    valor :: int as total_var
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
                    descripcion as nivel_or
                from
                    naty
                    join codigo_valor as c on (id_codigo_valor :: text = valor)
                where
                    id_columna = 55
                group by
                    cueanexo,
                    escuela,
                    id_fila,
                    descripcion
                order by
                    cueanexo
            ) as nivel_or USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    descripcion as grado_anio
                from
                    naty
                    join codigo_valor as c on (id_codigo_valor :: text = valor)
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
                    valor :: int as edad_5
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
            ) as edad_5 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_6
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
            ) as edad_6 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_7
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
            ) as edad_7 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_8
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
            ) as edad_8 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_9
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
            ) as edad_9 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_10
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
            ) as edad_10 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_11
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
            ) as edad_11 USING (cueanexo, id_fila)
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
                    escuela,
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
                    escuela,
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
                    escuela,
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
                    escuela,
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
                    escuela,
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
                    escuela,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as edad_17 USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as edad_18_y_mas
                from
                    naty
                where
                    id_columna = 104
                group by
                    cueanexo,
                    escuela,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as edad_18_y_mas USING (cueanexo, id_fila)
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
                    valor :: int as var_rep
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
                    valor :: int as tot_alum_promoasis
                from
                    naty
                where
                    id_columna = 708
                group by
                    cueanexo,
                    escuela,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as tot_alum_promoasis USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as var_alum_promoasis
                from
                    naty
                where
                    id_columna = 709
                group by
                    cueanexo,
                    escuela,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as var_alum_promoasis USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as tot_discapacidad
                from
                    naty
                where
                    id_columna = 870
                group by
                    cueanexo,
                    escuela,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as tot_discapacidad USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as var_discapacidad
                from
                    naty
                where
                    id_columna = 871
                group by
                    cueanexo,
                    escuela,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as var_discapacidad USING (cueanexo, id_fila)
        )        
    ORDER BY
        cueanexo,
        id_fila
) --end create view