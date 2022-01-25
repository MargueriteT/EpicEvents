from rest_framework import permissions


class ContractPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_authenticated and \
               request.user.status == 'Sale' or request.user.status == \
               'Management'
        elif request.method == 'POST':
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
            if obj.sale_user == request.user:
                return True
            if request.user.status == 'Management':
                return True



