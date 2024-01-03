from rest_framework.permissions import BasePermission

class OwnerBy(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsManager(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager')


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='manager') or request.user.is_superuser


class IsCustomer(BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='customer')
