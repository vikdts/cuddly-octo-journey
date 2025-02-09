from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.
class ProfileList(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        return Response(serializer.data)
