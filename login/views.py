from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, LoginSerializer

@api_view(['GET'])
def login(request):
  if request.method == 'GET':
    try:
      if request.GET['nickname'] and request.GET['password']:
        user_nickname = request.GET['nickname']
        user_password = request.GET['password']
        try:
          user = User.objects.get(pk=user_nickname)
        except:
          return Reponse(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LoginSerializer(user)
        return Response(serializer.data)    
    except:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
@api_view(['POST'])
def register(request):
  if request.method == 'POST':
    new_user = request.data
    serializer = UserSerializer(data=new_user)

    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data, status=status.HTTP_201_CREATED)
    else: 
      Reponse(status=status.HTTP_400_BAD_REQUEST)