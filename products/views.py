from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from .models import Category,Products,Cart
from .serializers import ProductSerializer,CategorySerializer,CartSerializer

# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
