from rest_framework import serializers

from products.models import Product, ProductImage

class ProductGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', )

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    genres = ProductGenreSerializer(many=True, required=False)
    is_favorite = serializers.BooleanField(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)
