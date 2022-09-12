CREATE OR replace FUNCTION consulta_cuadro(cuadro int,relevamiento varchar)
RETURNS TABLE( cueanexo VARCHAR(10), escuela VARCHAR(500),id_definicion_cuadro VARCHAR(20),
			 id_fila int,fila VARCHAR(500), id_columna int,columna varchar(200),valor varchar(700)) AS
$BODY$
DECLARE
    reg RECORD;
BEGIN
    FOR reg IN 
	select * 
from dblink ('dbname='||relevamiento||' user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' ::text, 
			 'SELECT loc.cueanexo, loc.escuela, --loc.oferta, 
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
             (datcuadro.id_definicion_cuadro='||cuadro||') 
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
             (defcel.id_definicion_cuadro='||cuadro||') 
       ORDER BY id_datos_cuadro asc, defcel.id_definicion_fila asc) AS cuadro USING (id_datos_cuadro)
ORDER BY loc.cueanexo asc,id_fila,id_columna' ::text)
             as matricula (cueanexo varchar,escuela varchar, id_definicion_cuadro varchar, id_fila varchar, 
						fila varchar,id_columna varchar,columna varchar, valor varchar)
	LOOP
        cueanexo := reg.cueanexo;
        escuela   := reg.escuela;
		id_definicion_cuadro   := reg.id_definicion_cuadro;
		id_fila   := reg.id_fila;
		fila   := reg.fila;
		id_columna   := reg.id_columna;
		columna := reg.columna;
		valor   := reg.valor;
        RETURN NEXT;
    END LOOP;
    RETURN;
END
$BODY$ LANGUAGE 'plpgsql'

-- select * from consulta_cuadro(104,'ra_carga2021')