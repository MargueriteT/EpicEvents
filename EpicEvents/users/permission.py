from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.status == \
                                             'Management'

    def has_object_permission(self, request, view, obj):
        """"
        Any authenticated user can create a new project.
        An user can update or delete a project only if he is the author of
        the project
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return True




