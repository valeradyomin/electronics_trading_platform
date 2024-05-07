from django.db import models
from treenode.models import TreeNodeModel
from django.utils.translation import gettext_lazy as _


class Structure(models.TextChoices):
    FACTORY = 'завод', _('завод')
    RETAIL = 'розничная сеть', _('розничная сеть')
    INDIVIDUAL = 'индивидуальный предприниматель', _('индивидуальный предприниматель')


class Supplier(TreeNodeModel):
    name = models.CharField(max_length=255, verbose_name='название поставщика')
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=255, verbose_name='номер дома')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='долг', default=0.0)
    supplier_structure = models.CharField(
        max_length=255,
        verbose_name='структура поставщика',
        choices=Structure.choices,
        default=Structure.FACTORY
    )

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='название товара')
    model = models.CharField(max_length=255, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='поставщик')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name
