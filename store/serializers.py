from rest_framework import serializers
from .models import Produto, Pedido, ItemPedido, Pagamento


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"


class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), source="produto", write_only=True)

    class Meta:
        model = ItemPedido
        fields = ["id", "produto", "produto_id", "quantidade", "preco_unitario", "subtotal"]
        read_only_fields = ["id", "subtotal", "preco_unitario"]


class PedidoSerializer(serializers.ModelSerializer):
    itens = ItemPedidoSerializer(many=True)
    total = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)

    class Meta:
        model = Pedido
        fields = ["id", "usuario", "data_criacao", "status", "total", "itens"]
        read_only_fields = ["id", "usuario", "data_criacao", "status", "total"]

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        user = self.context["request"].user
        pedido = Pedido.objects.create(usuario=user)
        for item in itens_data:
            produto = item["produto"]
            quantidade = item["quantidade"]
            if quantidade > produto.estoque:
                raise serializers.ValidationError("Estoque insuficiente para alguns itens.")
            ItemPedido.objects.create(
                pedido=pedido,
                produto=produto,
                quantidade=quantidade,
                preco_unitario=produto.preco,
            )
            produto.estoque -= quantidade
            produto.save()
        pedido.calcular_total()
        pedido.save()
        return pedido


class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = "__all__"
        read_only_fields = ["id", "data"] 