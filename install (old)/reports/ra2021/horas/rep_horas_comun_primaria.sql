create view rep_horas_comun_primaria as (
with naty as (
	select * from consulta_cuadro(140,'ra_carga2021')
)
select row_number() over () as id, * from (
(select cueanexo,escuela,id_fila,fila as cargos, valor as total from naty 
where id_columna = 5 group by cueanexo,escuela,id_fila,fila,valor order by cueanexo) as total
LEFT JOIN 
(select cueanexo,id_fila, valor as titular from naty 
where id_columna = 41 group by cueanexo,escuela,id_fila,valor order by cueanexo) as titular
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as interinos from naty 
where id_columna = 42 or id_columna = 139 group by cueanexo,escuela,id_fila,valor order by cueanexo) as interinos
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as sin_cubrir from naty 
where id_columna = 43 group by cueanexo,escuela,id_fila,valor order by cueanexo) as sin_cubrir
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as contratados from naty 
where id_columna = 44 group by cueanexo,escuela,id_fila,valor order by cueanexo) as contratados
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as planes_programas from naty 
where id_columna = 45 group by cueanexo,escuela,id_fila,valor order by cueanexo) as planes_programas
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as itinerantes from naty 
where id_columna = 54 group by cueanexo,escuela,id_fila,valor order by cueanexo) as itinerantes
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as pasantias from naty 
where id_columna = 73 group by cueanexo,escuela,id_fila,valor order by cueanexo) as pasantias
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
) order by cueanexo,id_fila )