from rest_framework import permissions


class SaleClientOrReadOnly(permissions.BasePermission):
    """"
    A sale user can oview any contract and create a new one. He's allowed to
    update a contract only if he's the owner. He can't delete contracts.
    """

    def has_permission(self, request, view):
        if request.method == 'DELETE':
            return False

        return request.user and request.user.is_authenticated and \
                       request.user.status == 'Sale'

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.sale_user


class ManagementClientOrReadOnly(permissions.BasePermission):
    """"
    A management user can view, create, update or delete any contract
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               request.user.status == 'Management'

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' or request.method == 'GET' or \
                request.method == 'DELETE':
            return True


class SupportClientOrReadOnly(permissions.BasePermission):
    """"
    A support user can only view client.
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_authenticated and \
                   request.user.status == 'Support'

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        else:
            return False


