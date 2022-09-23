


- instalar dblink en db visualizador -> CREATE EXTENSION dblink;
- la funcion consulta_cuadro install/funcion_cuadro_remote.sql
- en db visualizador ejecutar /install/mapa/rellenar_tabla_mapa_padron.sql
- en db vializador imrpotar en la tabla t_localizaciones /install/mapa/t_localizaciones_4326.csv
    (tiene encabezado, separado por coma, econding 'Latin1')
- crear base de datos por cada ra_cargaXXXX
- instalar dblink en cada ra_cargaXXXX -> CREATE EXTENSION dblink;
- ejecutar los sql reports/XXXX/*.sql
- 
