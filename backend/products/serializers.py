from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    categoryName = serializers.CharField(source="category_name")
    seoUrl       = serializers.SlugField(source="seo_url")

    class Meta:
        model  = Category
        fields = ["id", "categoryName", "seoUrl"]


class ProductSerializer(serializers.ModelSerializer):
    categoryId      = serializers.PrimaryKeyRelatedField(source="category", queryset=Category.objects.all())
    productName     = serializers.CharField(source="product_name")
    quantityPerUnit = serializers.CharField(source="quantity_per_unit")
    unitPrice       = serializers.DecimalField(source="unit_price", max_digits=10, decimal_places=2)
    unitsInStock    = serializers.IntegerField(source="units_in_stock")

    class Meta:
        model  = Product
        fields = ["id", "categoryId", "productName", "quantityPerUnit", "unitPrice", "unitsInStock"]
