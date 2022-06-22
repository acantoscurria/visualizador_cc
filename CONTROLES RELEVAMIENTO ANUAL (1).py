#!/usr/bin/env python
# coding: utf-8

# ![ESCUELA](C:\Users\Pablo\visualizador\iconoescuelasprimaria.jpg)

# In[1]:


import psycopg2
import pandas as pd
import io
import  numpy  as  np
import matplotlib.pyplot as plt


# In[ ]:


# DATOS DE BASE RA2021DATAFRAME CARGOS DOCENTES - CONSULTA PARA CONTROL DIRECTOR
conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
matricula = "select cueanexo, cuadernillo, nivel, cargos, total::int from cargos_docentes_ra22_prueba where (cargos ilike 'Director' or cargos ilike 'Director con clase anexa' or cargos ilike 'Director Maestro (Personal único)' or cargos ilike 'Director maestro con clase anexa' or cargos ilike 'Director/Rector' or cargos ilike 'Rector / Director' or cargos ilike 'Regente')"
director = pd.read_sql(matricula,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
# CONTROL DE DIRECTORES
df_director = pd.crosstab(index= director.cueanexo,
                  columns = director.cargos,
                  values= director.total,
                  aggfunc ="sum").fillna(0)
df_director['Control'] = df_director['Director']  + df_director['Director maestro con clase anexa'] + df_director['Rector / Director'] +df_director['Regente']+df_director['Director con clase anexa']+df_director['Director Maestro (Personal único)']
df_cont=df_director['Control']>1
df_control = df_director[df_cont]
df_control.head()


# In[ ]:


# CONTROL DE DIRECTORES EN ANEXO
conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
matricula = """select cueanexo, SUBSTRING("cueanexo",8)as anexo, cuadernillo, nivel, cargos, total::int from cargos_docentes_ra22_prueba where (cargos ilike 'Director' or cargos ilike 'Director con clase anexa' or cargos ilike 'Director Maestro (Personal único)' or cargos ilike 'Director maestro con clase anexa' or cargos ilike 'Director/Rector' or cargos ilike 'Rector / Director' or cargos ilike 'Regente')   """
df_anexo = pd.read_sql(matricula,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
df_1 = df_anexo['anexo']!= '00' 
df_anexo = df_anexo[df_1]
df_2 = df_anexo['total']== 1
df_anexo = df_anexo[df_2]
df_anexo.head()


# In[ ]:


#CONTROL BIBLIOTECARIO
conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
matricula = "select cueanexo, cuadernillo, nivel, cargos, total from cargos_docentes_ra22_prueba where (nivel!= 'Común - Servicios Complementarios' and cargos ilike 'Bibliotecario' and total::int >0)"
biblioteca = pd.read_sql(matricula,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
#df_cont1 = biblioteca['nivel']!= 'Común - Servicios Complementarios'
#df_control_1 = biblioteca[df_cont1]
#df_control_1
biblioteca.head()


# # CONTROL TRAYECTORIA MATRICULA SECUNDARIA

# In[ ]:


# DATOS DE BASE RA2021 DATAFRAME CARGOS DOCENTES - CONSULTA PARA CONTROL DIRECTOR
conn = psycopg2.connect("dbname=RA_2021 user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
mat_sec = "select cueanexo, año_est, sum(total::int) as RA_total_mat  FROM matric_comun_secundaria group by cueanexo, año_est "
mat_sec = pd.read_sql(mat_sec,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
tray_sec = "select cueanexo, año as año_est, sum(total_matric::int) as Total_Mat_inicial FROM RA22_trayec_comun_secundaria group by cueanexo, año "
tray_sec = pd.read_sql(tray_sec,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
df_control_tray = pd.merge(tray_sec, mat_sec, on=["cueanexo", "año_est"])
df_control_tray['control'] = df_control_tray.apply(lambda x: abs(x['total_mat_inicial']-x["ra_total_mat"]), axis = 1)
control_tray = df_control_tray['control']>0
df_control_tray = df_control_tray[control_tray]
df_control_tray.head()


# # CONTROL TRAYECTORIA MATRICULA PRIMARIA

# In[ ]:


# DATOS DE BASE RA2021 DATAFRAME CARGOS DOCENTES - CONSULTA PARA CONTROL DIRECTOR
conn = psycopg2.connect("dbname=RA_2021 user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
mat_prim = "select cueanexo, grado_año, sum(total::int) as ra_total  FROM matric_comun_primaria group by cueanexo, grado_año "
mat_prim = pd.read_sql(mat_prim,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
tray_prim = "select cueanexo, fila as grado_año, sum(total_matric::int) as Total_Mat FROM RA22_trayec_comun_primaria group by cueanexo, grado_año "
tray_prim = pd.read_sql(tray_prim,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
vector_1 = tray_prim['grado_año']=='1°'
vector_2 = tray_prim['grado_año']=='2°'
vector_3 = tray_prim['grado_año']=='3°'
vector_4 = tray_prim['grado_año']=='4°'
vector_5 = tray_prim['grado_año']=='5°'
vector_6 = tray_prim['grado_año']=='6°'
vector_7 = tray_prim['grado_año']=='7°'
tray_prim.loc[vector_1, 'grado_año'] = '1ro Año/Grado'
tray_prim.loc[vector_2, 'grado_año'] = '2do Año/Grado'
tray_prim.loc[vector_3, 'grado_año'] = '3er Año/Grado'
tray_prim.loc[vector_4, 'grado_año'] = '4to Año/Grado'
tray_prim.loc[vector_5, 'grado_año'] = '5to Año/Grado'
tray_prim.loc[vector_6, 'grado_año'] = '6to Año/Grado'
tray_prim.loc[vector_7, 'grado_año'] = '7mo Año/Grado'
df_control_tray_prim = pd.merge(tray_prim, mat_prim, on=["cueanexo", "grado_año"])
df_control_tray_prim['control'] = df_control_tray_prim.apply(lambda x: abs(x['total_mat']-x["ra_total"]), axis = 1)
control_tray = df_control_tray_prim['control']>0
df_control_tray_prim = df_control_tray_prim[control_tray]
df_control_tray_prim.head()


# # CONTROL - Alumnos provenientes de ámbito rural

# In[ ]:


conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
mat_rural= """ select *  FROM ra22_matricula_rural """
mat_rural = pd.read_sql(mat_rural,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
mat_rural[['cueanexo', 'escuela', 'total_rural', 'total_var',  'fecha_creac_establec', 'region', 'cui', 'sector', 'ambito','numero', 'localidad', 'departamento', 'cod_postal', 'categoria','estado_est', 'estado_loc']]


# In[ ]:


conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
mat_albergue= """ select *  FROM ra22_albergue """
mat_albergue = pd.read_sql(mat_albergue,con = conn,  index_col= "cueanexo") #objeto leer sql
conn.close()
mat_albergue[['nivel','sector','ambito','total']]


# # CONTROL Secciones Inical

# In[32]:


conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
MatSeccInical= """ select *  FROM ra22_secciones_comun_inicial where tipo_secc ilike 'Mult%' """
MatSeccInical = pd.read_sql(MatSeccInical,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
MatSeccInical[['0','1','2','3','4','5']]= MatSeccInical['matricula'].str.split('-',expand=True)
MatSeccInical['control']= MatSeccInical[['0','1','2','3','4','5']].count(axis=1)
ControlMatSeccInical = MatSeccInical['control']<=1
MatSeccInical = MatSeccInical[ControlMatSeccInical]
MatSeccInical[['cueanexo','escuela','tipo_secc','nom_secc','salas','0','1','2','3','4','5','control']]


# # CONTROL Secciones Primaria

# In[42]:


conn = psycopg2.connect("dbname=visualizador user=visualizador password=Estadisticas23 host=sigechaco.com.ar port=5432")
MatSeccPrimaria= """ select *  FROM ra22_secciones_comun_primaria where tipo_secc ilike 'Mult%' """
MatSeccPrimaria = pd.read_sql(MatSeccPrimaria,con = conn)#,  index_col= "cueanexo") #objeto leer sql
conn.close()
MatSeccPrimaria[['0','1','2','3','4','5','6']]= MatSeccPrimaria['matricula'].str.split('-',expand=True)
MatSeccPrimaria['control']= MatSeccPrimaria[['0','1','2','3','4','5']].count(axis=1)
ControlMatSeccPrimaria = MatSeccPrimaria['control']<=1
MatSeccPrimaria = MatSeccPrimaria[ControlMatSeccPrimaria]
MatSeccPrimaria[['cueanexo','escuela','tipo_secc','nombre_secc','grado_año','0','1','2','3','4','5','control']]


# In[37]:


MatSeccPrimaria


# In[ ]:




