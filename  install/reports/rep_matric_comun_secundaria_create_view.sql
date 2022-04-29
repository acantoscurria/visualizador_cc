create view rep_matric_comun_secundaria as (
with naty as (
SELECT loc.cueanexo, loc.escuela, --loc.oferta, 
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
             (datcuadro.id_definicion_cuadro='158') --and cueanexo='220007900' --OR (datcuadro.id_definicion_cuadro='593'))
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
             (defcel.id_definicion_cuadro='158') --OR (defcel.id_definicion_cuadro='593'))
       ORDER BY id_datos_cuadro asc, defcel.id_definicion_fila asc) AS cuadro USING (id_datos_cuadro)
ORDER BY loc.cueanexo asc,id_fila,id_columna
)
select row_number() over () as id, * from (
(select cueanexo,id_fila,descripcion  as turno
from naty join codigo_valor as cv on (id_codigo_valor = valor::int)
where id_columna = 2
group by cueanexo,id_fila,descripcion
order by cueanexo ) as turno
LEFT JOIN
(select cueanexo,id_fila,valor::int  as total
from naty 
where id_columna = 5
group by cueanexo,id_fila,valor
order by cueanexo ) as total
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as total_var
from naty 
where id_columna = 7
group by cueanexo,id_fila,valor
order by cueanexo ) as varones
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,descripcion  as nivel
from naty join codigo_valor as cv on (valor::int = id_codigo_valor)
where id_columna = 55
group by cueanexo,id_fila,descripcion
order by cueanexo ) as nivel
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int as edad_12
from naty 
where id_columna = 98
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_12
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_13
from naty 
where id_columna = 99
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_13
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_14
from naty 
where id_columna = 100
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_14
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_15
from naty 
where id_columna = 101
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_15
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_16
from naty 
where id_columna = 102
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_16
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_17
from naty 
where id_columna = 103
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_17
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as total_rep
from naty 
where id_columna = 127
group by cueanexo,id_fila,valor
order by cueanexo ) as total_rep
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as var_rep
from naty 
where id_columna = 128
group by cueanexo,id_fila,valor
order by cueanexo ) as var_rep
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as nro_orden_pe
from naty 
where id_columna = 165
group by cueanexo,id_fila,valor
order by cueanexo ) as nro_orden_pe
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,descripcion  as anio_est
from naty join codigo_valor as cv on(id_codigo_valor = valor::int)
where id_columna = 166
group by cueanexo,id_fila,descripcion
order by cueanexo ) as anio_est
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor  as nom_div
from naty 
where id_columna = 173
group by cueanexo,id_fila,valor
order by cueanexo ) as nom_div
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,descripcion  as tipo_div
from naty join codigo_valor as cv on (valor::int = id_codigo_valor)
where id_columna = 174
group by cueanexo,id_fila,descripcion
order by cueanexo ) as tipo_div
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,descripcion  as orientacion
from naty join codigo_valor as cv on (valor::int = id_codigo_valor)
where id_columna = 175
group by cueanexo,id_fila,descripcion
order by cueanexo ) as orientacion
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_11_y_menos
from naty 
where id_columna = 177
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_11_y_menos
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_18
from naty 
where id_columna = 178
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_18
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_19
from naty 
where id_columna = 179
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_19
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_25_y_mas
from naty 
where id_columna = 181
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_25_y_mas
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as edad_20_24
from naty 
where id_columna = 301
group by cueanexo,id_fila,valor
order by cueanexo ) as edad_20_24
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor  as denom_pe
from naty 
where id_columna = 551
group by cueanexo,id_fila,valor
order by cueanexo ) as denom_pe
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as total_disc
from naty 
where id_columna = 870
group by cueanexo,id_fila,valor
order by cueanexo ) as total_disc
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor::int  as var_disc
from naty 
where id_columna = 871
group by cueanexo,id_fila,valor
order by cueanexo ) as var_disc
USING (cueanexo,id_fila)
 ) LEFT JOIN
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