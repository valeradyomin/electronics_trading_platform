from rest_framework.exceptions import ValidationError


def validate_supplier_structure(value):
    if value == 'завод':
        return value


class SupplierStructureValidator:
    def __call__(self, attrs):
        supplier_structure = validate_supplier_structure(attrs['supplier_structure'])
        if supplier_structure == 'завод' and attrs.get('tn_parent') is not None:
            raise ValidationError("Завод не может быть дочерним элементом сети.")
        return attrs


class DebtUpdateValidator:
    def __call__(self, value):
        if value.get('debt'):
            raise ValidationError("Обновление задолженности перед поставщиком запрещено.")
