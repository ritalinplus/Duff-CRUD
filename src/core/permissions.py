from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = "Must be the owner"

    def has_object_permission(self, request, view, obj):
        """Gives permission for not safe methods (GET, HEAD and OPTION) only if the authenticated user is the owner
        of the object.

        Args:
            request (Request): Django Rest Framework request
            view (ViewSet): Django Rest Framework viewSet
            obj (Model): Django database model object.

        Return:
            bool: True if request method is safe or if authenticated user if the owner. False otherwise.

        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.owner
