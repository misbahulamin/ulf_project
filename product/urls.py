from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, SubCategoryViewSet, ColorViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubCategoryViewSet)
router.register(r'colors', ColorViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

