from rest_framework import permissions
from .roles import Role

class BaseRolePermission(permissions.BasePermission):
    def has_role(self, user, role: Role) -> bool:
        return user and user.role == role.value

class IsAdmin(BaseRolePermission):
    def has_permission(self, request, view):
        return self.has_role(request.user, Role.ADMIN)

class IsManager(BaseRolePermission):
    def has_permission(self, request, view):
        return self.has_role(request.user, Role.MANAGER)

class HasRolePermission(permissions.BasePermission):
    def __init__(self, required_permission: str):
        self.required_permission = required_permission

    def has_permission(self, request, view):
        return request.user and request.user.has_role_permission(self.required_permission)