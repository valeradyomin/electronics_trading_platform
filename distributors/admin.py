from treenode.admin import TreeNodeModelAdmin, TreeNodeForm

from .models import Supplier, Product
from django.contrib import admin
from django.contrib import messages
from django.urls import reverse
from django.utils.html import format_html


def clear_debt(modeladmin, request, queryset):
    """Очистить задолженность перед поставщиком"""
    for supplier in queryset:
        supplier.debt = 0
        supplier.save()
    messages.success(request, "Задолженность перед поставщиком успешно очищена.")


clear_debt.short_description = "Очистить задолженность перед поставщиком"


class SupplierAdminForm(TreeNodeForm):
    """Форма для редактирования поставщиков"""
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierAdmin(TreeNodeModelAdmin):
    """Админка поставщиков"""
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_ACCORDION
    # treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_BREADCRUMBS
    treenode_display_mode = TreeNodeModelAdmin.TREENODE_DISPLAY_MODE_INDENTATION

    list_display = ('name', 'supplier_structure', 'email', 'tn_parent', 'debt', 'get_supplier_link')
    list_display_links = ('name',)
    list_filter = ('city',)

    form = SupplierAdminForm
    list_per_page = 100
    # ordering = ['tn_parent']
    actions = [clear_debt]

    def get_supplier_link(self, obj):
        """Ссылка на поставщика"""
        supplier_id = obj.tn_parent.id if obj.tn_parent else obj.id
        url = reverse("admin:distributors_supplier_change", args=[supplier_id])
        return format_html('<a href=%s>%s</a>' % (url, obj.tn_parent))

    get_supplier_link.short_description = 'Ссылка на поставщика'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка продуктов"""
    list_display = ('name', 'model', 'release_date', 'supplier')


admin.site.register(Supplier, SupplierAdmin)
