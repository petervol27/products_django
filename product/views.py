from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from .serializers import ProductSerializer


# Create your views here.
def show_products(request):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)
