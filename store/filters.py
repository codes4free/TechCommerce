from django_filters import rest_framework as filters
from .models import Produto

class ProdutoFilter(filters.FilterSet):
    preco_min = filters.NumberFilter(field_name="preco", lookup_expr="gte")
    preco_max = filters.NumberFilter(field_name="preco", lookup_expr="lte")
    estoque_min = filters.NumberFilter(field_name="estoque", lookup_expr="gte")

    class Meta:
        model = Produto
        fields = ["preco_min", "preco_max", "estoque_min"]
