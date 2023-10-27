from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit their own profile"""
        # checks if the change is in safe methods
        if request.method in permissions.SAFE_METHODS:
            return True
            # checks if user changes own profile
        return obj.id == request.user.id
