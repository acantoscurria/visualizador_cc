create view rep_matric_aborigen as(
with naty as (
select * from consulta_cuadro(519,'ra_carga2021')
), codigo_valor as (select * from dblink ('dbname=ra_carga2021 user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' ::text, 
										  'select id_codigo_valor, descripcion
										  from codigo_valor' ::text)
             									as codigo_valor (id_codigo_valor int,descripcion varchar) )
select row_number() over () as id, cueanexo,'Especial' as tipo_ed,'Todos los Niveles' as nivel,escuela,sum(total::int) as total,sum(total_var::int) as tot_var, --LINEA PARA OBTENER INICIAL
-- total,total_var,
nro_est,anio_creac_establec,fecha_creac_establec,region,udt,cui,
cua,cuof,sector,ambito,ref_loc,calle,numero,localidad,departamento,cod_postal,categoria,estado_est,
estado_loc,telefono_cod_area,telefono_nro,per_funcionamiento,email_loc from (
(select cueanexo,escuela,id_fila,valor  as total
from naty --join codigo_valor as cv on (id_codigo_valor = valor::int)
where id_columna = 5
group by cueanexo,escuela,id_fila,valor
order by cueanexo ) as total
LEFT JOIN
(select cueanexo,id_fila,valor  as total_var
from naty
where id_columna = 7 
group by cueanexo,id_fila,valor
order by cueanexo ) as total_var
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
) AS p using (cueanexo))
group by total.cueanexo,escuela,nom_est,nro_est,anio_creac_establec,fecha_creac_establec,region,udt,cui, --LINEAS PARA OBTENER INICIAL
cua,cuof,sector,ambito,ref_loc,calle,numero,localidad,departamento,cod_postal,categoria,estado_est,
estado_loc,telefono_cod_area,telefono_nro,per_funcionamiento,email_loc
order by total.cueanexo
	)