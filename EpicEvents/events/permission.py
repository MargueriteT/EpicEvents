from rest_framework import permissions


class SaleAndManagementEventPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
                   request.user.status == 'Sale' or request.user.status == \
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
            if request.user.status == 'Sale' and obj.sale_user == request.user:
                return True
            if request.user.status == 'Management':
                return True


class SupportEventPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'PUT':
            return request.user and request.user.is_authenticated and \
               request.user.status == 'Support'

    def has_object_permission(self, request, view, obj):
        """"
        Any authenticated user can create a new project.
        An user can update or delete a project only if he is the author of
        the project
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.support_user == request.user:
                return True

