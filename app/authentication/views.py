from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.models import User
from authentication.serializers import RegisterSerializer, UserSerializer


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=serializer.data["email"]).first():
                return Response({"detail": "email already registered"}, status=status.HTTP_400_BAD_REQUEST)
            print(serializer)
            user = serializer.validated_data
            user.save()
            token = RefreshToken.for_user(user)

            print(token.token)
            return Response({"data": UserSerializer(user).data, "access": str(token.access_token), "refresh": str(token)},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    model = User
    def get(self, request, *args, **kwargs):
        user = request.user
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)