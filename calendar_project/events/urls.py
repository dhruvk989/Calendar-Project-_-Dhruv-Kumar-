# events/urls.py

from django.urls import path
from .views import CalendarEventViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', CalendarEventViewSet, basename='events')

urlpatterns = router.urls
