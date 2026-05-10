import json, os
from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        path = os.path.join(os.path.dirname(__file__), "../../../db.json")
        with open(path) as f:
            data = json.load(f)

        category_map = {}
        for c in data["categories"]:
            obj, _ = Category.objects.get_or_create(
                seo_url=c["seoUrl"],
                defaults={"category_name": c["categoryName"]},
            )
            category_map[str(c["id"])] = obj

        if not Product.objects.exists():
            for p in data["products"]:
                Product.objects.create(
                    category=category_map.get(str(p["categoryId"])),
                    product_name=p["productName"],
                    quantity_per_unit=p["quantityPerUnit"],
                    unit_price=p["unitPrice"],
                    units_in_stock=p["unitsInStock"],
                )
