from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Order,OrderItem
from .serializers import OrderSerializer 

# Create your views here.
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
