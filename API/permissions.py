from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """Allow access only to Admin users."""
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsOwner(BasePermission):
    """Allow access only to the owner of the object."""
    def has_object_permission(self, request, view, obj):
        return obj == request.user
