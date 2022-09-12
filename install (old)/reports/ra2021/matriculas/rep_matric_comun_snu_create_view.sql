create view rep_matric_comun_snu as (
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
             (datcuadro.id_definicion_cuadro='287') --and cueanexo='220007900' --OR (datcuadro.id_definicion_cuadro='593'))
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
             (defcel.id_definicion_cuadro='287') --OR (defcel.id_definicion_cuadro='593'))
       ORDER BY id_datos_cuadro asc, defcel.id_definicion_fila asc) AS cuadro USING (id_datos_cuadro)
ORDER BY loc.cueanexo asc,id_fila,id_columna
)
select row_number() over () as id, * from (
(select cueanexo,escuela,id_fila, valor as n_plan_estudio from naty 
where id_columna = 165 group by cueanexo,escuela,id_fila,valor order by cueanexo) as n_plan_estudio
LEFT JOIN
(select cueanexo,id_fila, valor as plan_est_titulo from naty 
where id_columna = 551 group by cueanexo,escuela,id_fila,valor order by cueanexo) as plan_est_titulo
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, descripcion as tipo_carrera from naty 
join codigo_valor as c on (id_codigo_valor::text = valor)
where id_columna = 291 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as tipo_carrera
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, descripcion as tipo_formacion from naty 
join codigo_valor as c on (id_codigo_valor::text = valor)
where id_columna = 292 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as tipo_formacion
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, descripcion as modalidad_dicatado from naty 
join codigo_valor as c on (id_codigo_valor::text = valor)
where id_columna = 188 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as modalidad_dicatado
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, descripcion as carrera_termino from naty 
join codigo_valor as c on (id_codigo_valor::text = valor)
where id_columna = 293 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as carrera_termino
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as total from naty 
where id_columna = 5 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as total_var from naty 
where id_columna = 7 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total_var
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as menos_18_años from naty 
where id_columna = 338 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  menos_18_años
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_18 from naty 
where id_columna = 178 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_18
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_19 from naty 
where id_columna = 179 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_19
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_20 from naty 
where id_columna = 339 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_20
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_21 from naty 
where id_columna = 341 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_21
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_22 from naty 
where id_columna = 343 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_22
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_23 from naty 
where id_columna = 346 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_23
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_24 from naty 
where id_columna = 348 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_24
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_25 from naty 
where id_columna = 491 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_25
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_26 from naty 
where id_columna = 492 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_26
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_27 from naty 
where id_columna = 493 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_27
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_28 from naty 
where id_columna = 877 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_28
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_29 from naty 
where id_columna = 878 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_29
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as edad_30 from naty 
where id_columna = 357 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  edad_30
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as total_ingresante from naty 
where id_columna = 365 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  total_ingresante
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as var_ingresante from naty 
where id_columna = 366 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  var_ingresante
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as total_pasantia_practicas from naty 
where id_columna = 370 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  total_pasantia_practica
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as var_pasantia_practicas from naty 
where id_columna = 373 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  var_pasantia_practica
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as total_residencia from naty 
where id_columna = 877 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  total_residencia
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as var_residencia from naty 
where id_columna = 878 group by cueanexo,escuela,id_fila,valor order by cueanexo) as  var_residencia
USING (cueanexo,id_fila)

	LEFT JOIN
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
) AS p using (cueanexo)
 ) ORDER BY cueanexo, id_fila
	)