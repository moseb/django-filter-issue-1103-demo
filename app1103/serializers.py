from rest_framework.serializers import ModelSerializer

from app1103.models import Product, ProductTag


class ProductTagSerializer(ModelSerializer):
    class Meta:
        model = ProductTag
        fields = [
            'id',
        ]


class ProductSerializer(ModelSerializer):
    tags = ProductTagSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'tags',
        ]
