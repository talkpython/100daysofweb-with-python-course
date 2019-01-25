from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # GET requests are allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # but write permissions are only allowed to the owner of a quote
        return obj.user == request.user
