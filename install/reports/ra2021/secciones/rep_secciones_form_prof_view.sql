create view rep_secciones_form_prof as(
with naty as (
	select * from consulta_cuadro(669,'ra_carga2021')
)
select row_number() over () as id, * from (
(select cueanexo,escuela,id_fila,fila as nivel, valor as total from naty 
where id_columna = 5 group by cueanexo,escuela,id_fila,fila,valor order by cueanexo) as total
LEFT JOIN 
(select cueanexo,id_fila, valor as varones from naty 
where id_columna = 7 group by cueanexo,escuela,id_fila,valor order by cueanexo) as varones
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as independientes_multiplan from naty 
where id_columna = 198 group by cueanexo,escuela,id_fila,valor order by cueanexo) as independientes_multiplan
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila, valor as multiples from naty 
where id_columna = 199 group by cueanexo,escuela,id_fila,valor order by cueanexo) as multiples
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