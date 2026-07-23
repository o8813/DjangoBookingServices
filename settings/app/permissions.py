from rest_framework.permissions import BasePermission

class IsHotelOwner(BasePermission):
    message = 'U have no rights for this action'

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.status == 'Owner'
        )

class IsOwnerOfHotel(BasePermission):
    message = 'U are not owner of this hotel'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user.id