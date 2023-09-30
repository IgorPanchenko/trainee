from django.urls import path

from api.views import ProductViewSet

urlpatterns = [
    path('lessons/', ProductViewSet.as_view({'get': 'list'}))
]