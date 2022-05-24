from rest_framework.permissions import BasePermission, SAFE_METHODS


# class IsCommentAuthor(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user or request.user.is_superuser == obj.user


class IsAdminClinic(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )

