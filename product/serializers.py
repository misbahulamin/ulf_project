from rest_framework import serializers
from .models import Category, SubCategory, Color, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'hex_code']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    sub_category = SubCategorySerializer()
    colors = ColorSerializer(many=True)  # Serialize many-to-many relationship

    class Meta:
        model = Product
        fields = [
            'id', 'product_code', 'title', 'quantity', 'colors','image', 'description',
            'size', 'sold_item', 'available_item', 'category', 'sub_category',
            'price', 'wholesale_price', 'special_offers', 'delivery_time'
        ]

class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    colors = serializers.PrimaryKeyRelatedField(queryset=Color.objects.all(), many=True)

    class Meta:
        model = Product
        fields = [
            'product_code', 'title', 'quantity', 'colors','image', 'description', 
            'size', 'sold_item', 'available_item', 'category', 'sub_category', 
            'price', 'wholesale_price', 'special_offers', 'delivery_time'
        ]

    def create(self, validated_data):
        colors = validated_data.pop('colors', [])
        product = Product.objects.create(**validated_data)
        product.colors.set(colors)
        return product

    def update(self, instance, validated_data):
        colors = validated_data.pop('colors', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.colors.set(colors)
        instance.save()
        return instance
