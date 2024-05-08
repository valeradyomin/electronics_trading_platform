from rest_framework import viewsets, filters


from distributors.models import Supplier, Product
from distributors.paginators import DistributorsPagination
from distributors.permissions import IsActiveEmployee
from distributors.serializers import SupplierSerializer, ProductSerializer


# Create your views here.


class SupplierViewSet(viewsets.ModelViewSet):
    """Представление для поставщиков"""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsActiveEmployee]
    pagination_class = DistributorsPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['country']
    ordering_fields = ['country']

    def get_queryset(self):
        """Фильтрация по стране"""
        queryset = Supplier.objects.all()

        country = self.request.query_params.get('country', None)
        if country is not None:
            queryset = queryset.filter(country=country)

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    """Представление для товаров"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveEmployee]
    pagination_class = DistributorsPagination
