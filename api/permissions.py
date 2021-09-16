from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # return super().has_object_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.listener is None:
            return True
        
        return obj.listener == request.user