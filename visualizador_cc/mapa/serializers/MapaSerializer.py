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

class TablaLocalizacionesSearchSerializer(geoSerilizer.GeoFeatureModelSerializer):

    class Meta:
        model=TablaLocalizaciones
        fields= '__all__'
        geo_field='geom'


    def get_properties(self, instance, fields):
        
        return (
            instance.cueanexo.nom_est,
            instance.cueanexo.ambito        
        )

    def unformat_geojson(self, feature):
        attrs = {     
            "nom_est": feature["properties"]   
                   
        }
        return attrs