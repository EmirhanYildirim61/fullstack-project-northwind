from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryListView, ProductViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"products", ProductViewSet, basename="product")

urlpatterns = [
    path("categories", CategoryListView.as_view()),
] + router.urls
