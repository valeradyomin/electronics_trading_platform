from rest_framework import permissions

from users.models import UserRoles


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        accepted_roles = [UserRoles.MEMBER, UserRoles.MODERATOR, UserRoles.ADMINISTRATOR]
        return request.user.is_active and request.user.role in accepted_roles
