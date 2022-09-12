create view rep_matric_especial_inicial as (
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
             (datcuadro.id_definicion_cuadro='844') --and cueanexo='220007900' --OR (datcuadro.id_definicion_cuadro='593'))
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
             (defcel.id_definicion_cuadro='844') --OR (defcel.id_definicion_cuadro='593'))
       ORDER BY id_datos_cuadro asc, defcel.id_definicion_fila asc) AS cuadro USING (id_datos_cuadro)
ORDER BY loc.cueanexo asc,id_fila,id_columna
)
select row_number() over () as id, * from (
(select cueanexo,escuela,id_fila, descripcion as sala from naty 
join codigo_valor as b on (id_codigo_valor::text = valor)
where id_columna = 1 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as sala
LEFT JOIN 
(select cueanexo,id_fila, descripcion as turno from naty
join codigo_valor as b on (id_codigo_valor::text = valor)
where id_columna = 2 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as turno
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, descripcion as tipo_secc from naty
join codigo_valor as b on (id_codigo_valor::text = valor)
where id_columna = 4 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as tipo_secc
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
(select cueanexo,id_fila, valor as nom_secc from naty
where id_columna = 90 group by cueanexo,escuela,id_fila,valor order by cueanexo) as nom_secc
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as cinco_anios from naty
where id_columna = 91 group by cueanexo,escuela,id_fila,valor order by cueanexo) as cinco_anios
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as seis_anios from naty
where id_columna = 92 group by cueanexo,escuela,id_fila,valor order by cueanexo) as seis_anios
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as siete_anios from naty
where id_columna = 93 group by cueanexo,escuela,id_fila,valor order by cueanexo) as siete_anios
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as cero_a_dos_anios from naty
where id_columna = 322 group by cueanexo,escuela,id_fila,valor order by cueanexo) as cero_a_dos_anios
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as tres_anios from naty
where id_columna = 481 group by cueanexo,escuela,id_fila,valor order by cueanexo) as tres_anios
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as cuatro_anios from naty
where id_columna = 482 group by cueanexo,escuela,id_fila,valor order by cueanexo) as cuatro_anios
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as ocho_o_mas_anios from naty
where id_columna = 814 group by cueanexo,escuela,id_fila,valor order by cueanexo) as ocho_o_mas_anios
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