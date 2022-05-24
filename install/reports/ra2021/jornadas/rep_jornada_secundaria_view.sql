create view rep_jornada_secundaria as(
select * from (
with naty as (
select *
from consulta_cuadro(165,'ra_carga2021')
), codigo_valor as (select * from dblink ('dbname=ra_carga2021 user=admin password=redfie11 host=201.217.244.102 port=5432' ::text, 
										  'select id_codigo_valor, descripcion
										  from codigo_valor' ::text)
             									as codigo_valor (id_codigo_valor int,descripcion varchar) )
select row_number() over () as id, jornada.cueanexo::int,id_fila,escuela,
case 
when fila = 'Jardín de Infantes'then replace(fila,'Infantes','infantes')
when fila = 'Jardín Maternal'then replace(fila,'Maternal','maternal')
when fila = 'Primario'then replace(fila,'Primario','Primaria')
when fila = 'Secundario / Medio / Polimodal' then replace(fila,'Secundario / Medio / Polimodal','Secundaria')
end as oferta
,total_je,horas_sem_jc,horas_sem_je,cant_alum_jc,con_disc_je,con_disc_jc
from (
(select cueanexo,escuela,id_fila,fila,valor  as total_je
from naty --join codigo_valor as cv on (id_codigo_valor = valor::int)
where id_columna = 28
group by cueanexo,escuela,id_fila,fila,valor
order by cueanexo ) as total_je
LEFT JOIN
(select cueanexo,id_fila,valor  as horas_sem_jc
from naty
where id_columna = 29
group by cueanexo,id_fila,valor
order by cueanexo ) as horas_sem_jc
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor  as horas_sem_je
from naty
where id_columna = 134
group by cueanexo,id_fila,valor
order by cueanexo ) as horas_sem_je
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor  as cant_alum_jc
from naty
where id_columna = 135
group by cueanexo,id_fila,valor
order by cueanexo ) as cant_alum_jc
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor  as con_disc_je
from naty
where id_columna = 804
group by cueanexo,id_fila,valor
order by cueanexo ) as con_disc_je
USING (cueanexo,id_fila)
LEFT JOIN
(select cueanexo,id_fila,valor  as con_disc_jc
from naty
where id_columna = 805
group by cueanexo,id_fila,valor
order by cueanexo ) as con_disc_jc
USING (cueanexo,id_fila)
) as jornada ) as jce
left join 
(select distinct cueanexo,nom_est,
-- SUBSTRING(oferta from 9 for (length(oferta)-9)) as oferta
case
	when oferta = 'Común - Primaria de 7 años ' then 'Primaria'
	when oferta = 'Común - Secundaria Completa req. 7 años ' then 'Secundaria'
	when oferta = 'Común - Jardín de infantes ' then 'Jardín de infantes'
	when oferta = 'Común - Jardín maternal ' then 'Jardín maternal'
end oferta,jornada
,ambito,sector,region_loc,ref_loc,
calle,numero,localidad,departamento,estado_loc,est_oferta,estado_est 
from padron_ofertas 
-- where oferta ilike 'Común%Primaria%'
where oferta ilike 'Común%Jar%' or oferta ilike 'Común%Primaria%' or oferta = 'Común - Secundaria Completa req. 7 años '
-- where  oferta = 'Común - Secundaria Completa req. 7 años '
) as p
using(cueanexo,oferta))