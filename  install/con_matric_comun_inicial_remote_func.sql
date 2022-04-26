create
or replace view public.con_matric_comun_inicial as (
    with naty as (
        select
            *
        from
            consulta_cuadro(104, 'ra_carga2022')
    ),
    codigo_valor as (
        select
            *
        from
            dblink (
                'dbname=ra_carga2022 user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' :: text,
                'select id_codigo_valor, descripcion
										  from codigo_valor' :: text
            ) as codigo_valor (id_codigo_valor int, descripcion varchar)
    )
    select
        row_number() over () as id, 
        'Común' as tipo_ed,
        'Inicial' as nivel,
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
                    join codigo_valor as cv on (id_codigo_valor = valor :: int)
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
                    join codigo_valor as cv on (id_codigo_valor = valor :: int)
                where
                    id_columna = 2
                group by
                    cueanexo,
                    id_fila,
                    descripcion
                order by
                    cueanexo
            ) as turno USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor as nom_secc
                from
                    naty
                where
                    id_columna = 3
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as nom_secc USING (cueanexo, id_fila)
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
                    valor :: int as menos_1_año
                from
                    naty
                where
                    id_columna = 8
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as menos_1_año USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as un_año
                from
                    naty
                where
                    id_columna = 9
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as un_año USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as dos_años
                from
                    naty
                where
                    id_columna = 10
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as dos_años USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as tres_años
                from
                    naty
                where
                    id_columna = 11
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as tres_años USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as cuatro_años
                from
                    naty
                where
                    id_columna = 12
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as cuatro_años USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as cinco_años
                from
                    naty
                where
                    id_columna = 13
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as cinco_años USING (cueanexo, id_fila)
            LEFT JOIN (
                select
                    cueanexo,
                    id_fila,
                    valor :: int as seis_años
                from
                    naty
                where
                    id_columna = 14
                group by
                    cueanexo,
                    id_fila,
                    valor
                order by
                    cueanexo
            ) as seis_años USING (cueanexo, id_fila)
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
)--end create view