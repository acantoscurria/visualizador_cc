from django.contrib.gis import admin
from leaflet.admin import LeafletGeoAdmin
from .models import TablaLocalizaciones,Padron


class TablaLocalizacioesAdmin(LeafletGeoAdmin):
    search_fields = ['nom_est','cueanexo']


admin.site.register(TablaLocalizaciones, TablaLocalizacioesAdmin)
admin.site.register(Padron)
