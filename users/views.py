from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer, UserSerializer, UserTokenPairSerializer
from utils.helper import writeResponse
# Create your views here.


class RegisterApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return writeResponse(status_code=status.HTTP_201_CREATED, message='OK', data=UserSerializer(user, context=serializer.context).data)


class UserTokenPairApiView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UserTokenPairSerializer

    # def post(self, request, format=False):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid()
    #     print('AJDKAJDK', serializer.data)
