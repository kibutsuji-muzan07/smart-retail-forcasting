from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import ProductAnalytics


# Create your views here.
@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"})


@api_view(['GET'])
def product_list(request):

    product = ProductAnalytics.objects.all().order_by("id")
    serializer = ProductSerializer(product, many=True)

    return Response(
        {
            "count": ProductAnalytics.objects.count(),
            "result": serializer.data,
        }
        )