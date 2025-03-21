from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from favorite.views import ManageFavorite
from app.permissions import IsOwnerOrReadOnly
from products.models import Product, ProductImage, Genre
from products.serializers import ProductSerializer, ProductImageSerializer, ProductGenreSerializer


class ProductView(viewsets.ModelViewSet, ManageFavorite):
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = self.annotate_qs_is_favorite_field(queryset)
        return queryset


class ProductImageView(viewsets.ModelViewSet ):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class GenreView(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = ProductGenreSerializer

    @action(
        methods=['get'],
        detail=True,
        url_path='products',
        permission_classes=(IsAuthenticated,),
        name='products-by-genre',
    )
    def products(self, request, pk=None):
        products = Product.objects.filter(genres=pk)
        serializer = ProductSerializer(products, many=True)
        paginator = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(paginator)
