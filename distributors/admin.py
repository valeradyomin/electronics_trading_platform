from treenode.admin import TreeNodeModelAdmin, TreeNodeForm

from .models import Supplier, Product
from django.contrib import admin
from django.contrib import messages


def clear_debt(modeladmin, request, queryset):
    for supplier in queryset:
        supplier.debt = 0
        supplier.save()
    messages.success(request, "Задолженность перед поставщиком успешно очищена.")


clear_debt.short_description = "Очистить задолженность перед поставщиком"


class SupplierAdminForm(TreeNodeForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierAdmin(TreeNodeModelAdmin):
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION

    list_display = ('name', 'supplier_structure', 'email', 'tn_parent', 'debt')
    list_display_links = ('name',)
    list_filter = ('city',)

    form = SupplierAdminForm
    list_per_page = 100
    # ordering = ['tn_parent']
    actions = [clear_debt]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'supplier')


admin.site.register(Supplier, SupplierAdmin)
