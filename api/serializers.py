from rest_framework.serializers import ModelSerializer
from app.models import Product, Lesson


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title']

