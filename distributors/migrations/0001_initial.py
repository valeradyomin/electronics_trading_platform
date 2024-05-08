# Generated by Django 4.2.7 on 2024-05-08 19:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tn_ancestors_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Ancestors pks')),
                ('tn_ancestors_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Ancestors count')),
                ('tn_children_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Children pks')),
                ('tn_children_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Children count')),
                ('tn_depth', models.PositiveIntegerField(default=0, editable=False, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Depth')),
                ('tn_descendants_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Descendants pks')),
                ('tn_descendants_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Descendants count')),
                ('tn_index', models.PositiveIntegerField(default=0, editable=False, verbose_name='Index')),
                ('tn_level', models.PositiveIntegerField(default=1, editable=False, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Level')),
                ('tn_priority', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)], verbose_name='Priority')),
                ('tn_order', models.PositiveIntegerField(default=0, editable=False, verbose_name='Order')),
                ('tn_siblings_pks', models.TextField(blank=True, default='', editable=False, verbose_name='Siblings pks')),
                ('tn_siblings_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Siblings count')),
                ('name', models.CharField(max_length=255, verbose_name='название поставщика')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='электронная почта')),
                ('country', models.CharField(max_length=255, verbose_name='страна')),
                ('city', models.CharField(max_length=255, verbose_name='город')),
                ('street', models.CharField(max_length=255, verbose_name='улица')),
                ('house_number', models.CharField(max_length=255, verbose_name='номер дома')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='долг')),
                ('supplier_structure', models.CharField(choices=[('завод', 'завод'), ('розничная сеть', 'розничная сеть'), ('индивидуальный предприниматель', 'индивидуальный предприниматель')], default='завод', max_length=255, verbose_name='категория поставщика')),
                ('tn_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tn_children', to='distributors.supplier', verbose_name='родительский поставщик')),
            ],
            options={
                'verbose_name': 'поставщик',
                'verbose_name_plural': 'поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название товара')),
                ('model', models.CharField(max_length=255, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='distributors.supplier', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
