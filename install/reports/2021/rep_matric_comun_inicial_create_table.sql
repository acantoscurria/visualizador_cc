create table rep_matric_comun_inicial as (
	with naty as (
		select
			*
		from
			consulta_cuadro(104, 'ra_carga2021')
	),
	codigo_valor as (
		select
			*
		from
			dblink (
				'dbname=ra_carga2021 user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' :: text,
				'select id_codigo_valor, descripcion
										  from codigo_valor' :: text
			) as codigo_valor (id_codigo_valor int, descripcion varchar)
	)
	select
		row_number() over () as id,	
		*
	from
		(
			(
				select
					cueanexo,
					escuela,
					id_fila,
					descripcion as sala
				from
					naty
					join codigo_valor as cv on (id_codigo_valor = valor :: int)
				where
					id_columna = 1
				group by
					cueanexo,
					escuela,
					id_fila,
					descripcion
				order by
					cueanexo
			) as sala
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					descripcion as turno
				from
					naty
					join codigo_valor as cv on (id_codigo_valor = valor :: int)
				where
					id_columna = 2
				group by
					cueanexo,
					id_fila,
					descripcion
				order by
					cueanexo
			) as turno USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor as nom_secc
				from
					naty
				where
					id_columna = 3
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as nom_secc USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					descripcion as tipo_secc
				from
					naty
					join codigo_valor as cv on (valor :: int = id_codigo_valor)
				where
					id_columna = 4
				group by
					cueanexo,
					id_fila,
					descripcion
				order by
					cueanexo
			) as tipo_secc USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as total
				from
					naty
				where
					id_columna = 5
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as total USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as total_var
				from
					naty
				where
					id_columna = 7
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as varones USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as menos_1_anio
				from
					naty
				where
					id_columna = 8
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as menos_1_anio USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as un_anio
				from
					naty
				where
					id_columna = 9
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as un_anio USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as dos_anios
				from
					naty
				where
					id_columna = 10
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as dos_anios USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as tres_anios
				from
					naty
				where
					id_columna = 11
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as tres_anios USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as cuatro_anios
				from
					naty
				where
					id_columna = 12
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as cuatro_anios USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as cinco_anios
				from
					naty
				where
					id_columna = 13
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as cinco_anios USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as seis_anios
				from
					naty
				where
					id_columna = 14
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as seis_anios USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as total_disc
				from
					naty
				where
					id_columna = 870
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as total_disc USING (cueanexo, id_fila)
			LEFT JOIN (
				select
					cueanexo,
					id_fila,
					valor :: int as var_disc
				from
					naty
				where
					id_columna = 871
				group by
					cueanexo,
					id_fila,
					valor
				order by
					cueanexo
			) as var_disc USING (cueanexo, id_fila)
		)
		LEFT JOIN (
			select
				*
			from
				dblink (
					'dbname=padron user=admin password=redfie11 host=relevamientoanual.com.ar port=5432' :: text,
					'select distinct cueanexo,nom_est,nro_est,anio_creac_establec,fecha_creac_establec,region,udt,cui,
cua,cuof,sector,ambito,ref_loc,calle,numero,localidad,departamento,cod_postal,categoria,estado_est,
estado_loc,telefono_cod_area,telefono_nro,per_funcionamiento,email_loc from padron' :: text
				) as padron (
					cueanexo varchar,
					nom_est varchar,
					nro_est varchar,
					anio_creac_establec varchar,
					fecha_creac_establec varchar,
					region varchar,
					udt varchar,
					cui varchar,
					cua varchar,
					cuof varchar,
					sector varchar,
					ambito varchar,
					ref_loc varchar,
					calle varchar,
					numero varchar,
					localidad varchar,
					departamento varchar,
					cod_postal varchar,
					categoria varchar,
					estado_est varchar,
					estado_loc varchar,
					telefono_cod_area varchar,
					telefono_nro varchar,
					per_funcionamiento varchar,
					email_loc varchar
				)
		) AS p using (cueanexo)
	ORDER BY
		cueanexo,
		id_fila
)