from rest_framework.permissions import BasePermission

class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return True
        
    def has_object_permission(self, request, view, obj):
        # if obj.employer_id == request.user :
        #     return True
        # else:
            return False
        
