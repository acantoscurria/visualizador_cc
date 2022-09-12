create view rep_matric_comun_primaria as (

with naty as (SELECT loc.cueanexo, loc.escuela, --loc.oferta, 
       loc.id_definicion_cuadro, cuadro.id_fila, cuadro.fila, 
       cuadro.id_columna, cuadro.columna, cuadro.valor 
FROM (-----------------------------------Cuadro, por cuadernillo, por localizacion, por Oferta----------------------------------
       SELECT distinct l.cueanexo, l.nombre as escuela, --defcap.c_oferta_agregada as oferta, 
              datcuader.id_datos_cuadernillo, datcuadro.id_definicion_cuadro, datcuadro.id_datos_cuadro  
       FROM definicion_capitulo as defcap, 
            localizacion as l LEFT JOIN datos_cuadernillo as datcuader using (id_localizacion)
                              LEFT JOIN datos_capitulo as datcap using (id_datos_cuadernillo)
                              LEFT JOIN datos_cuadro as datcuadro using (id_datos_capitulo)
       WHERE (defcap.id_definicion_cuadernillo=datcuader.id_definicion_cuadernillo) AND 
             --(
             (datcuadro.id_definicion_cuadro='626') --and cueanexo='220007900' --OR (datcuadro.id_definicion_cuadro='593'))
       order by l.cueanexo asc, datcuadro.id_datos_cuadro asc ) AS loc LEFT JOIN (
       -------------------------------------Valor de celdas, por CUADRO----------------------------------------------------------
       SELECT defcel.id_definicion_cuadro, datcel.id_datos_cuadro, 
              defcel.id_definicion_fila as id_fila, deffil.nombre as fila, 
              defcel.id_definicion_columna as id_columna, defcol.nombre as columna, datcel.valor
       FROM datos_celda as datcel, 
            definicion_columna as defcol left join definicion_celda as defcel using (id_definicion_columna)
                                         left join definicion_fila as deffil using (id_definicion_fila)
       WHERE (datcel.id_definicion_celda=defcel.id_definicion_celda) AND 
             --(
             (defcel.id_definicion_cuadro='626') --OR (defcel.id_definicion_cuadro='593'))
       ORDER BY id_datos_cuadro asc, defcel.id_definicion_fila asc) AS cuadro USING (id_datos_cuadro)
ORDER BY loc.cueanexo asc,id_fila,id_columna
)
select row_number() over () as id, * from (
(select cueanexo,escuela,id_fila, descripcion as turno from naty 
join codigo_valor as b on (id_codigo_valor::text = valor)
where id_columna = 2 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as turno
LEFT JOIN 
(select cueanexo,id_fila, valor as nombre_secc from naty 
where id_columna = 3 group by cueanexo,escuela,id_fila,valor order by cueanexo) as nombre_secc
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, descripcion as tipo_secc from naty 
join codigo_valor as c on (id_codigo_valor::text = valor)
where id_columna = 4 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as tipo_secc
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as total from naty 
where id_columna = 5 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as total_var from naty 
where id_columna = 7 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total_var
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, descripcion as nivel from naty 
join codigo_valor as c on (id_codigo_valor::text = valor)
where id_columna = 55 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as nivel
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, descripcion as grado_anio from naty 
join codigo_valor as c on (id_codigo_valor::text = valor)
where id_columna = 89 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as grado_anio
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_5 from naty 
where id_columna = 91 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_5
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_6 from naty 
where id_columna = 92 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_6
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_7 from naty 
where id_columna = 93 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_7
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_8 from naty 
where id_columna = 94 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_8
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_9 from naty 
where id_columna = 95 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_9
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_10 from naty 
where id_columna = 96 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_10
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_11 from naty 
where id_columna = 97 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_11
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_12 from naty 
where id_columna = 98 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_12
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_13 from naty 
where id_columna = 99 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_13
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_14 from naty 
where id_columna = 100 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_14
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_15 from naty 
where id_columna = 101 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_15
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_16 from naty 
where id_columna = 102 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_16
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_17 from naty 
where id_columna = 103 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_17
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as edad_18_y_mas from naty 
where id_columna = 104 group by cueanexo,escuela,id_fila,valor order by cueanexo) as edad_18_y_mas
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as total_rep from naty 
where id_columna = 127 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total_rep
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as var_rep from naty 
where id_columna = 128 group by cueanexo,escuela,id_fila,valor order by cueanexo) as var_rep
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as tot_alum_promoasis from naty 
where id_columna = 708 group by cueanexo,escuela,id_fila,valor order by cueanexo) as tot_alum_promoasis
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as var_alum_promoasis from naty 
where id_columna = 709 group by cueanexo,escuela,id_fila,valor order by cueanexo) as var_alum_promoasis
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as tot_discapacidad from naty 
where id_columna = 870 group by cueanexo,escuela,id_fila,valor order by cueanexo) as tot_discapacidad
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor::int as var_discapacidad from naty 
where id_columna = 871 group by cueanexo,escuela,id_fila,valor order by cueanexo) as var_discapacidad
USING (cueanexo,id_fila)
)LEFT JOIN
(select * 
from dblink ('dbname=padron user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' ::text, 'select distinct cueanexo,nom_est,nro_est,anio_creac_establec,fecha_creac_establec,region,udt,cui,
cua,cuof,sector,ambito,ref_loc,calle,numero,localidad,departamento,cod_postal,categoria,estado_est,
estado_loc,telefono_cod_area,telefono_nro,per_funcionamiento,email_loc from padron' ::text)
             as padron (cueanexo varchar,nom_est varchar,nro_est varchar,anio_creac_establec varchar,
						fecha_creac_establec varchar,region varchar,udt varchar,cui varchar,
						cua varchar,cuof varchar,sector varchar,ambito varchar,ref_loc varchar,
						calle varchar,numero varchar,localidad varchar,departamento varchar,
						cod_postal varchar,categoria varchar,estado_est varchar,estado_loc varchar,
						telefono_cod_area varchar,telefono_nro varchar,per_funcionamiento varchar,email_loc varchar)
) AS p using (cueanexo) order by cueanexo,id_fila --)
	)
