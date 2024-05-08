from rest_framework import serializers

from distributors.models import Supplier, Product
from distributors.validators import SupplierStructureValidator, DebtUpdateValidator


class SupplierSerializer(serializers.ModelSerializer):
    """ Сериализатор для поставщиков """
    class Meta:
        model = Supplier
        # fields = '__all__'
        fields = ['id', 'name', 'supplier_structure', 'debt', 'tn_parent']
        validators = [SupplierStructureValidator(), DebtUpdateValidator()]


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для товаров """
    class Meta:
        model = Product
        fields = '__all__'
