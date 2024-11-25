from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,CategoryViewSet,CartViewSet

router = DefaultRouter()
router.register('products',ProductViewSet)
router.register('category',CategoryViewSet)
router.register('cart', CartViewSet)


urlpatterns = [
    path('',include(router.urls))
]


