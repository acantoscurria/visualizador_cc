from rest_framework import serializers
from rest_framework_gis import serializers as geoSerilizer
from visualizador_cc.mapa.models import Padron,TablaLocalizaciones
# from rest_framework_gis import 

class PadronOfertaSerializer(serializers.ModelSerializer):

    class Meta:
        model= Padron
        fields= '__all__'


class TablaLocalizacionesSerializer(geoSerilizer.GeoFeatureModelSerializer):

    class Meta:
        model=TablaLocalizaciones
        fields= '__all__'
        geo_field='geom'


    # def get_properties(self, instance, fields):
        
    #     return (
    #     instance.cueanexo.nom_est,
    #     instance.cueanexo.sector,
    #     instance.cueanexo.ambito,
    #     instance.cueanexo.region_loc,
    #     instance.cueanexo.localidad,
    #     instance.cueanexo.departamento,
    #     )

    # def unformat_geojson(self, feature):
    #     attrs = {
    #         self.Meta.geo_field: feature["geometry"],
    #         "nom_est": feature["properties"],
    #         "sector": feature["properties"],
    #         "ambito": feature["properties"],
    #         "region_loc": feature["properties"],
    #         "localidad": feature["properties"],
    #         "departamento": feature["properties"],
    #     }

    #     return attrs