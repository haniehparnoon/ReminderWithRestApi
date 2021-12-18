from rest_framework import permissions 
from rest_framework.permissions import BasePermission
from .models import *

# has_permisson - block user
# has object permission - 
#  safe method - doesn't affect on db
class IsOwnerOrReadOnly(BasePermission):
    # def has_permission(self, req):
    #     if req.method in permissions.SAFE_METHODS:

    def has_object_permission(self, request, view, obj):
        # if request.method in permissions.SAFE_METHODS and request.user.is_authenticated():
        #     return request.user == Task.objects.get(owner=request.owner)
        # else:
        return obj.owner == request.user



