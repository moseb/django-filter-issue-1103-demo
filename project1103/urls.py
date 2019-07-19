from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from app1103.views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
] + router.urls
