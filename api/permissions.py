from rest_framework import permissions
from .models import ADMIN


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.access_level == ADMIN
