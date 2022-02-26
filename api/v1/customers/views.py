from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView

from customers.models import UserProfile
from .serializers import UserProfileSerializer
from customers.renderers import ProfileJSONRenderer
from .exceptions import ProfileDoesNotExist

class UserProfileRetrieveAPIView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    renderer_classes = (ProfileJSONRenderer,)
    serializer_class = UserProfileSerializer
    
    def retrieve(self, request, username, *args, **kwargs):
        try:
            profile = UserProfile.objects.select_related('user').get(
                user__username=username
            )
        except UserProfile.DoesNotExist:
            raise ProfileDoesNotExist
        serializer = self.serializer_class(profile)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def update(self, request, *args, **kwargs):
        user_data = request.data.get('user', {})
        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'profile': {
               'bio': user_data.get('bio', request.user.profile.bio),
               'age': user_data.get('age', request.user.profile.age),
               'gender': user_data.get('gender', request.user.profile.gender),
               'phone': user_data.get('phone', request.user.profile.phone),
               'avatar': user_data.get('avatar', request.user.profile.avatar)
            }
        }
        serializer = self.serializer_class(
        request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
            
    