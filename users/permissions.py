from rest_framework import permissions
from rest_framework.views import Request, View
from users.models import User


class AuthOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated


class ListingRetrievingDestroyingPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "PATCH" or "DELETE":
            return request.user.is_authenticated and request.user.is_superuser


class ListingPermissionStaffCreating(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == "POST" and request.user.is_superuser is True:
            return True and request.user.is_authenticated


class StaffListingPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method == "GET" and request.user.is_superuser is True:
            return True
        elif request.method == "POST":
            return True


class StaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class StaffOrOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return obj.id == request.user.id or request.user.is_superuser
