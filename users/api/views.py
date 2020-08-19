from rest_framework.generics import ListAPIView
from users.models import Profile
from .serializers import ProfileSerializer

class ProfileListAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer