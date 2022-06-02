create view padron_ofertas as(
SELECT padron.cueanexo::integer AS cueanexo,
    padron.nom_est,
    padron.acronimo_oferta,
    padron.oferta,
    padron.nro_est,
    padron.ambito,
    padron.sector,
    padron.region_loc,
    padron.ref_loc,
    padron.calle,
    padron.numero,
    padron.localidad,
    padron.departamento,
    padron.estado_loc,
    padron.est_oferta,
    padron.estado_est,
    padron.jornada
   FROM dblink('dbname=padron user=admin password=redfie11 host=relevamientoanual.com.ar port=5432'::text, 'select distinct (cue||anexo) as cueanexo, nom_est,acronimo_oferta,oferta,nro_est,ambito,sector,region_loc,
			ref_loc,calle,numero,localidad,departamento,jornada,estado_loc,est_oferta,estado_est
			from padron_ofertas'::text) padron(cueanexo character varying, nom_est character varying, acronimo_oferta character varying, oferta character varying, nro_est character varying, ambito character varying, sector character varying, region_loc character varying, ref_loc character varying, calle character varying, numero character varying, localidad character varying, departamento character varying, jornada character varying, estado_loc character varying, est_oferta character varying, estado_est character varying))