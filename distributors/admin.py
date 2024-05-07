from django.contrib import admin
from treenode.admin import TreeNodeModelAdmin

from .models import Supplier, Product


class SupplierAdmin(TreeNodeModelAdmin):
    list_display = ('supplier_structure', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier')


admin.site.register(Supplier, SupplierAdmin)
