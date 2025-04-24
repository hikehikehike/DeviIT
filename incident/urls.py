from rest_framework.routers import DefaultRouter
from incident.views import IncidentViewSet, IncidentListViewSet

router = DefaultRouter()
router.register(r'incidents', IncidentViewSet, basename='incident')
router.register(r'incidents_geojson', IncidentListViewSet, basename='incident_geojson')

urlpatterns = router.urls
