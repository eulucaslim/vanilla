from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def show_product(request):
  if request.method == "GET":
    try:
      if request.GET['code_product']:
        code_product = request.GET['code_product']
        product = Product.objects.get(pk=code_product)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
      Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_product(request):
  if request.method ==  "POST":
    try:
      new_product = request.data
      serializer = ProductSerializer(data=new_product)

      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_product(request):
  if request.method == "PUT":
    try:
      code_product = request.data['code_product']
      update_product = Product.objects.get(pk=code_product)
      serializer = ProductSerializer(update_product, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
      else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
      return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def remove_product(request, code_product):
  if request.method == 'DELETE':
    try:
      product_to_delete = get_object_or_404(Product, pk=code_product)
      product_to_delete.delete()
      return Response(status=status.HTTP_202_ACCEPTED)
    except Exception as e:
      return Response({'error': f"Erro ao deletar o produto: {str(e)}"},
      status=status.HTTP_400_BAD_REQUEST)
