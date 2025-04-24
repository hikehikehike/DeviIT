from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from incident.models import Incident


class IncidentGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Incident
        geo_field = 'location'
        fields = ['id', 'name', 'status', 'created_at', 'location']


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['id', 'name', 'status', 'created_at', 'location']
