from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsNotAuthenticated(BasePermission):
    """
    Allows access if not authenticated.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_anonymous
