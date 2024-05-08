from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from distributors.models import Supplier, Product
from distributors.paginators import DistributorsPagination
from distributors.permissions import IsActiveEmployee
from distributors.serializers import SupplierSerializer, ProductSerializer


# Create your views here.


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveEmployee]
    pagination_class = DistributorsPagination


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveEmployee]
    pagination_class = DistributorsPagination
