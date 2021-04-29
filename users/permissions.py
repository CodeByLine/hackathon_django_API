from rest_framework import permissions


class ObjectPermission(permissions.BasePermission):
    """
    Checks that user is object owner
    """
    # pass
    def has_permission(self, request, view, obj):
        return obj.id == request.user




    def __init__(self, request, view):
        self.request = request
        self.view = view
        # return obj.id == request.user
        

    def has_perm(self, request, view, obj):
        # pass
        
        if request.method in permissions.SAFE_METHODS:
            # return True
        
        # Instance must have an attribute named `owner`.
            return obj.id == request.user
        else:
            return False
