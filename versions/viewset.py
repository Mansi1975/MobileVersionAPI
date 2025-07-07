from rest_framework import viewsets, permissions
from .models import MobileVersion
from .serializers import MobileVersionSerializer

class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
            return request.user and request.user.is_superuser
        return True  # allow GET on detail view for all

class MobileVersionViewSet(viewsets.ModelViewSet):
    queryset = MobileVersion.objects.all()
    serializer_class = MobileVersionSerializer
    lookup_field = 'version'
    permission_classes = [IsSuperUserOrReadOnly]
    lookup_value_regex = r'[^/]+'  # Allows any character except '/