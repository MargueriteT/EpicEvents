from rest_framework import permissions


class SaleContractOrReadOnly(permissions.BasePermission):
    """"
    A sale user can oview any contract and create a new one. He's allowed to
    update a contract only if he's the owner. He can't delete contracts.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and \
               request.user.status == 'Sale'

    def has_object_permission(self, request, view, obj):
        if request.method == 'PUT' and request.user == obj.sale_user:
            return True


class ManagementContractOrReadOnly(permissions.BasePermission):
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


class SupportContractOrReadOnly(permissions.BasePermission):
    """"
    A support user can only access to the contract list and read details
    about a contract. He can't create neither update a contract
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


