create view rep_egresados_adultos_secundaria as(
with naty as (
	select * from consulta_cuadro(458,'ra_carga2021')
), codigo_valor as (select * from dblink ('dbname=ra_carga2021 user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' ::text, 
										  'select id_codigo_valor, descripcion
										  from codigo_valor' ::text)
             									as codigo_valor (id_codigo_valor int,descripcion varchar) )
select row_number() over () as id, 'Común' as tipo_ed, 'Secundaria' as nivel,  * from ( --CAMBIAR EN SELECT SEGÚN EL ID POR MODALIDAD ADULTOS/COMUN
(select cueanexo,escuela,id_fila, valor as nro_plan_est from naty
--join codigo_valor as b on (id_codigo_valor::text = valor)
where id_columna = 165 group by cueanexo,escuela,id_fila,valor order by cueanexo) as nro_plan_est
LEFT JOIN 
(select cueanexo,id_fila, descripcion as orientacion from naty
join codigo_valor as b on (id_codigo_valor::text = valor)
where id_columna = 175 group by cueanexo,escuela,id_fila,descripcion order by cueanexo) as orientacion
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as total_egresados_no_fines from naty
where id_columna = 216 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total_egresados_no_fines
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as total_var_egresados_no_fines from naty
where id_columna = 217 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total_var_egresados_no_fines
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as plan_est from naty
--join codigo_valor as b on (id_codigo_valor::text = valor)
where id_columna = 551 group by cueanexo,escuela,id_fila,valor order by cueanexo) as plan_est
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as titulo_nivel from naty
where id_columna = 559 group by cueanexo,escuela,id_fila,valor order by cueanexo) as titulo_nivel
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as total_egresados_dm from naty
where id_columna = 825 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total_egresados_dm
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as var_egresados_dm from naty
where id_columna = 826 group by cueanexo,escuela,id_fila,valor order by cueanexo) as var_egresados_dm
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as total_egresados_fines from naty
where id_columna = 827 group by cueanexo,escuela,id_fila,valor order by cueanexo) as total_egresados_fines
USING (cueanexo,id_fila)
LEFT JOIN 
(select cueanexo,id_fila, valor as var_egresados_fines from naty
where id_columna = 828 group by cueanexo,escuela,id_fila,valor order by cueanexo) as var_egresados_fines
USING (cueanexo,id_fila)

)
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
order by cueanexo,id_fila)