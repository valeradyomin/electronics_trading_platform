from django.db import models

# Create your models here.

NULLABLE = {
    'null': True,
    'blank': True,
}


class BaseContactInfo(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    country = models.CharField(max_length=255, verbose_name='страна')
    city = models.CharField(max_length=255, verbose_name='город')
    street = models.CharField(max_length=255, verbose_name='улица')
    house_number = models.CharField(max_length=255, verbose_name='номер дома')

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Supplier(BaseContactInfo):
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name='задолженность')


class TradeNetwork(BaseContactInfo):
    LEVEL_CHOICES = (
        (0, 'завод'),
        (1, 'розничная сеть'),
        (2, 'индивидуальный предприниматель'),
    )

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')
    level = models.IntegerField(choices=LEVEL_CHOICES, default=0, verbose_name='уровень сети')


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='название товара')
    model = models.CharField(max_length=255, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    network = models.ForeignKey(TradeNetwork, on_delete=models.CASCADE, verbose_name='торговая сеть')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return self.name