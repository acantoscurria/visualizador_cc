# from django.db import models
# from defer import defer
from django.contrib.gis.db import models


class Padron(models.Model):
    """
    Tabla que contendrá la mayor información sobre las localizaciones y se relaciona a uno 
    con t_localizaciones. Se actualiza por cron directamente.
    """
    cueanexo = models.BigIntegerField(verbose_name="CueAnexo del Establecimiento",primary_key=True)
    nom_est = models.CharField(verbose_name="Nombre del Establecimiento",null=True,blank=True,max_length=250)
    sector = models.CharField(null=True,blank=True,max_length=200) # privado, estattal, gestion social
    ambito = models.CharField(null=True,blank=True,max_length=100) # urbano, rural disperso y agromerado
    region_loc = models.CharField(null=True,blank=True,max_length=100) 
    localidad = models.CharField(null=True,blank=True,max_length=500)
    departamento = models.CharField(null=True,blank=True,max_length=500) # 
    estado_loc=models.CharField(verbose_name="Estado de la localización",blank=False,
    null=False,max_length=10)

    class Meta:
        managed = True
        verbose_name_plural = 'Datos de Padron'

    def __str__(self):
        return f'{self.cueanexo} - {self.nom_est} '


class TablaLocalizaciones(models.Model):
    """
    Modelo para la tabla t_localizaciones que mantiene el equipo de mapas
    """
    cueanexo = models.OneToOneField(to=Padron,verbose_name="Cueanexo", 
    help_text="Debe coincidir con cueanexo de sistema padron",
    primary_key=True,default=0,on_delete=models.CASCADE,db_column="cueanexo")

    geom = models.PointField(blank=True, null=True)

    search_fields = ('prop__txt')

    class Meta:
        managed = True
        db_table = 't_localizaciones'
        verbose_name_plural = 'Localizaciones'

    def __str__(self):
        return f'{self.cueanexo}'


    def parse(self):
        return {              
            'cueanexo': self.cueanexo.cueanexo,            
            'nom_est': self.cueanexo.nom_est,  
            'sector': self.cueanexo.sector,                 
            'ambito': self.cueanexo.ambito,  
            'region_loc': self.cueanexo.region_loc, 
            'localidad': self.cueanexo.localidad, 
            'departamento': self.cueanexo.departamento
        }
          