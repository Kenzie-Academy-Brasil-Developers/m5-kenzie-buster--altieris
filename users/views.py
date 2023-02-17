from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer

class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        
        serializer = UserSerializer(users, many=True)
        
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        try:
            if request.data['is_employee'] == True:
                user = User.objects.create_superuser(**serializer.validated_data)
            else:
                user = User.objects.create_user(**serializer.validated_data)
        except KeyError:
            user = User.objects.create_user(**serializer.validated_data)
            
        serializer = UserSerializer(user)
        
        return Response(serializer.data, status.HTTP_201_CREATED)