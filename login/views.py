from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def get_users(request):
  if request.method == 'GET':
    users = User.objects.all()
    serializers = UserSerializer(users, many=True)
    return Response(serializers.data)

  return Response(status=status.HTTP_404_NOT_FOUND) 

@api_view(['POST'])
def create_users(request):
  if request.method == 'POST':
    new_user = request.data
    serializer = UserSerializer(data=new_user)

    if serializer.is_valid():
      serializer.save()
      return Response (serializer.data, status=status.HTTP_201_CREATED)
    else: 
      Reponse(status=status.HTTP_400_BAD_REQUEST)
