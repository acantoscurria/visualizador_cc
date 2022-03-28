# from django.db import models
# from defer import defer
from ast import Mod
from django.contrib.gis.db import models
# from sqlalchemy import null


class PadronOferta(models.Model):
    oferta = models.BigIntegerField(primary_key=True,null=False,default=0)
    id_localizacion = models.BigIntegerField(null=False,default=0,
    help_text="Se debe obtener el id_establecimiento de sistema padron")
    nombre_oferta = models.CharField(verbose_name="Oferta del establecimiento",blank=False,
    null=False,default='',max_length=250)

    def __str__(self):
        return f'{self.oferta} - {self.nombre_oferta}'


class Padron(models.Model):
    id_localizacion = models.BigIntegerField(unique=True,null=False,default=0,
    primary_key=True,help_text="Se debe obtener el id_establecimiento de sistema padron")
    oferta = models.ManyToManyField(PadronOferta,verbose_name="Ofertas que tiene el Establecimiento",
    default=0)
    cueanexo = models.BigIntegerField(null=False,default=0)
    nom_est = models.CharField(null=True,blank=True,max_length=250)
    sector = models.CharField(null=True,blank=True,max_length=200)
    ambito = models.CharField(null=True,blank=True,max_length=100)
    region_loc = models.CharField(null=True,blank=True,max_length=100)
    localidad = models.CharField(null=True,blank=True,max_length=500)
    departamento = models.CharField(null=True,blank=True,max_length=500)

    class Meta:
        managed = True
        verbose_name_plural = 'Datos de Padron'
    
    def __str__(self):
        return f'{self.cueanexo} - {self.nom_est}'



class TablaLocalizaciones(models.Model):
    padron_est = models.OneToOneField(Padron,on_delete=models.CASCADE,
    primary_key=True,help_text="Se debe obtener el id_establecimiento de sistema padron",
    default=0)
    geom = models.PointField(srid=5347, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_localizaciones'
        verbose_name_plural = 'Localizaciones'

    def __str__(self):
        return f'{self.padron_est.cueanexo} - {self.padron_est.nom_est}'
