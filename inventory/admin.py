from django.contrib import admin
from .models import ProductAnalytics

# Register your models here.
@admin.register(ProductAnalytics)
class ProductAnalyticsAdmin(admin.ModelAdmin):
    list_display = (
        "product_id",
        "title",
        "category",
        "price",
        "stock",
        "inventory_value",
        "is_hot",
        "humidity",
        "holiday_count",
    )

    search_fields = ("title", "category")
    list_filter = ("category", "is_hot", "humidity")
