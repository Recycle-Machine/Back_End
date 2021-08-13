''' User edit permission '''

#Django REST framwork
from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token

#Models
from django.contrib.auth.models import User
from users.models import Profile

class IsOwnProfile(BasePermission):
    ''' Check if is owner '''

    def has_object_permission(self, request, view, obj):
        user_id = request.path.split('/')
        user_id = int(user_id[2])


        try:
            user = User.objects.get(username=request.user.username)
            if user.id == user_id:
                return True
        except User.DoesNotExist:
            return False