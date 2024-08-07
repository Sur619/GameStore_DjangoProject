from rest_framework import generics, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import logout


@permission_classes([])
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@permission_classes([])
class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


@permission_classes([])
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        request.auth.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
