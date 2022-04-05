# from django.db import models
# from defer import defer
from django.contrib.gis.db import models

class Padron(models.Model):
    """
    Tabla que contendrá la mayor información sobre las localizaciones y se relaciona a uno 
    con t_localizaciones. Se actualiza por cron directamente.
    """
    padron = models.BigIntegerField(default=0,primary_key=True)
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
        # unique_together = [['cueanexo','nom_est','ambito','sector']]
    
    
    def __str__(self):
        ofertas = []
        for of in self.oferta.values_list('nombre_oferta'):
            for oferta in of:
                ofertas.append(oferta)

        return f'{self.cueanexo} - {self.nom_est} - Ofertas: {ofertas}'
    
    # def natural_key(self):
    #     return (self.cueanexo, self.nom_est,self.ambito,self.sector)


class PadronOferta(models.Model):
    """
    Tabla que se actualizará automáticamente con la información de ofertaseducativas que ya 
    se encuentra en el sistema de padron. Se actualiza por cron directamente.
    """

    padron_id = models.ForeignKey(Padron,verbose_name="Localización",
    help_text="Elegir el establecimiento al que pertenece esta oferta",
    default=0,on_delete=models.CASCADE,related_name='oferta')

    oferta = models.BigIntegerField(verbose_name="ID de la oferta",primary_key=True,
    default=0,help_text="Este valor se debe obtener del sistema web Padron")

    nombre_oferta = models.CharField(verbose_name="Oferta del establecimiento",blank=False,
    null=False,default='',max_length=250)

    def __str__(self):

        return f'Oferta: {self.nombre_oferta} - Establecimiento: {self.padron_id.nom_est}'

class TablaLocalizaciones(models.Model):
    """
    Modelo para la tabla t_localizaciones que mantiene el equipo de mapas
    """
    establecimiento = models.OneToOneField(to=Padron,verbose_name="ID establecimiento", 
    help_text="Se debe completar con id establecimiento de padron web",
    primary_key=True,default=0,on_delete=models.CASCADE)

    geom = models.PointField(srid=5347, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 't_localizaciones'
        verbose_name_plural = 'Localizaciones'

    def __str__(self):
        return f'{self.establecimiento.cueanexo} - {self.establecimiento.nom_est}'
