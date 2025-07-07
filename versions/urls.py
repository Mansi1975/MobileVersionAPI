from rest_framework.routers import DefaultRouter
from .views import MobileVersionViewSet
from django.urls import path, include
from django.http import JsonResponse

router = DefaultRouter()
router.register(r'mobile-version', MobileVersionViewSet, basename='mobileversion')

# Allow dots in version field like 1.0.5
MobileVersionViewSet.lookup_field = 'version'
MobileVersionViewSet.lookup_value_regex = r'[\w\.]+'

urlpatterns = [
    path('', include(router.urls)),  # API endpoints
]
