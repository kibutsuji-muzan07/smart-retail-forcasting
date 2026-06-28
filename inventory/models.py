from django.db import models

class ProductAnalytics(models.Model):

    product_id = models.IntegerField()

    title = models.CharField(
        max_length=255
    )

    category = models.CharField(
        max_length=100
    )

    price = models.FloatField()

    stock = models.IntegerField()

    inventory_value = models.FloatField()

    is_hot = models.BooleanField()

    humidity = models.BooleanField()

    holiday_count = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "product_analytics"
