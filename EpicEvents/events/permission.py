from rest_framework import permissions


"""class SaleAndManagementEventPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
                   request.user.status == 'Sale' or request.user.status == \
                   'Management'

    def has_object_permission(self, request, view, obj):
    
        Any authenticated user can create a new project.
        An user can update or delete a project only if he is the author of
        the project
        
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

        Any authenticated user can create a new project.
        An user can update or delete a project only if he is the author of
        the project

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if obj.support_user == request.user:
                return True"""


class SaleEventOrReadOnly(permissions.BasePermission):

    """A sale user can oview any contract and create a new one. He's allowed to
    update a contract only if he's the owner. He can't delete contracts."""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               request.user.status == 'Sale'

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' and request.user == obj.sale_user:
            return True


class ManagementEventOrReadOnly(permissions.BasePermission):

    """A management user can view, create, update or delete any event"""

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               request.user.status == 'Management'

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' or request.method == 'GET' or \
                request.method == 'DELETE':
            return True


class SupportEventOrReadOnly(permissions.BasePermission):
    """"
    A support user can view events and details. He also can update is own
    events. He's not allowed to delete or create event.
    """

    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'PUT':
            return request.user and request.user.is_authenticated and \
                   request.user.status == 'Support'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.support_user:
            return True