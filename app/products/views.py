from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from products.models import Product, ProductImage
from products.serializers import ProductSerializer, ProductImageSerializer


class ProductView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(
     methods=['post'],
     detail=True,
     url_path='favorite',
    )
    def favorite(self, request, pk=None):
        pass


class ProductImageView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
