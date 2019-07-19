from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from app1103.models import Product
from app1103.serializers import ProductSerializer


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'tags': ['exact', 'in'],
        }


class ProductViewSet(GenericViewSet, ListModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
