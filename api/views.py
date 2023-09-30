from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import ProductSerializer
from app.models import Product

class ProductViewSet(ReadOnlyModelViewSet):
    """Получить список всех продуктов"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny, )
