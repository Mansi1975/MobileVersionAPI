from rest_framework import viewsets, permissions
from .models import MobileVersion
from .serializers import MobileVersionSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser

class MobileVersionViewSet(viewsets.ModelViewSet):
    queryset = MobileVersion.objects.all()
    serializer_class = MobileVersionSerializer
    lookup_field = 'version'
    permission_classes = [IsSuperUserOrReadOnly]
