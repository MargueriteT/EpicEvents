from rest_framework import permissions


class ClientPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_authenticated and \
               request.user.status == 'Sale' or request.user.status == \
               'Management' or request.user.status == 'Support'
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
        if request.method == 'GET':
            return True
        else:
            if request.user.status == 'Management' or request.user.status ==\
                    'Sale':
                return True



