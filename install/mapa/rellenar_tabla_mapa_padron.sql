SELECT  padron.cueanexo
       ,padron.nom_est
       ,padron.sector
       ,padron.ambito
       ,padron.region AS region_loc
       ,padron.localidad
       ,padron.departamento
       ,padron.estado_loc
       ,padron.ref_loc
       ,padron.calle
       ,padron.numero
       ,padron.cod_postal
       ,padron.email_loc
FROM dblink
('dbname=padron user=admin password=redfie11 host=relevamientoanual.com.ar port=5432'::text, '
	SELECT  distinct cueanexo
	       ,nom_est
	       ,sector
	       ,ambito
	       ,region
	       ,localidad
	       ,departamento
	       ,estado_loc
	       ,ref_loc
	       ,calle
	       ,numero
	       ,cod_postal
	       ,email_loc
	FROM padron'::text
) padron(cueanexo bigint, nom_est character varying, sector character varying, 
ambito character varying, region character varying, localidad character varying, 
departamento character varying, estado_loc character varying, ref_loc varchar, 
calle varchar, numero varchar, cod_postal varchar, email_loc varchar)