from rest_framework import serializers

from distributors.models import Supplier, Product


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        # fields = '__all__'
        fields = ['id', 'name', 'supplier_structure']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
