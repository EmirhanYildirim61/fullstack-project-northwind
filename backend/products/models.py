from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    seo_url       = models.SlugField(max_length=200, unique=True)


class Product(models.Model):
    category          = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_name      = models.CharField(max_length=200)
    quantity_per_unit = models.CharField(max_length=200)
    unit_price        = models.DecimalField(max_digits=10, decimal_places=2)
    units_in_stock    = models.IntegerField(default=0)
