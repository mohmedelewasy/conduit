from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import CreateAPIView
from profiles.models import Profile
from .serializers import RegistrationSerializers

from . import serializers

class RegisterView(CreateAPIView):
    model = Profile
    serializer_class = RegistrationSerializers

    def post(self, request, *args, **kwargs):
        if request.data['password'] == request.data['password2']:
            return super(RegisterView, self).post(request, *args, **kwargs)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)