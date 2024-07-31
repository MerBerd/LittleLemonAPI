from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class IsManager(BasePermission):
    def has_permission(self, request, view):
        allowed_groups = ['Manager']

        if request.user and request.user.is_authenticated:
            return request.user.groups.filter(name__in=allowed_groups).exists()
        
        return False