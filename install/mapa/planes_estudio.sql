
select * from (

(select cueanexo,'Común - Secundaria' as modalidad,regexp_replace(valor, '\d+', '', 'g') as plan_estudio 
from consulta_cuadro(157,'ra_carga2022')  where id_columna = 257)

UNION ALL

(select cueanexo,'Común - SNU' as modalidad,regexp_replace(valor, '\d+', '', 'g') as plan_estudio 
from consulta_cuadro(257,'ra_carga2022') where id_columna = 289)
) as planes
