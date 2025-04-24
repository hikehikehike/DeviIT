from rest_framework import viewsets
from incident.models import Incident
from incident.serializers import IncidentGeoSerializer, IncidentSerializer


class IncidentListViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Incident.objects.filter(status='active')
    serializer_class = IncidentGeoSerializer


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
