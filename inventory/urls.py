from django.urls import path
from .views import product_list, health_check

urlpatterns = [
    path("", health_check, name="health"),
    path('products', product_list, name='product-list'),
]