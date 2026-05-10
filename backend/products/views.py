from rest_framework import generics, viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListView(generics.ListAPIView):
    queryset         = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class   = ProductSerializer
    http_method_names  = ["get", "post", "put", "head", "options"]

    def get_queryset(self):
        qs          = Product.objects.all()
        category_id = self.request.query_params.get("categoryId")
        if category_id:
            qs = qs.filter(category_id=category_id)
        return qs
