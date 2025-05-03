# Placeholder tests for models. Replace with actual tests for 'subtotal' and 'calcular_total'.
import pytest
from store.models import Pedido, ItemPedido

def test_models_placeholder():
    assert True 

# Placeholder tests for API endpoints. Replace with actual tests.

def test_produtos_list():
    # Simulate test for GET /api/produtos/
    assert True

def test_pedidos_create():
    # Simulate test for POST /api/pedidos/ using JWT authentication
    assert True 

@pytest.mark.django_db

def test_pedido_total_and_str(product_factory, django_user_model):
    user = django_user_model.objects.create(username="foo")
    prod1 = product_factory(preco=10)
    prod2 = product_factory(preco=5)
    pedido = Pedido.objects.create(usuario=user)
    ItemPedido.objects.create(pedido=pedido, produto=prod1, quantidade=1, preco_unitario=10)
    ItemPedido.objects.create(pedido=pedido, produto=prod2, quantidade=3, preco_unitario=5)
    pedido.calcular_total()
    assert pedido.total == 25
    assert "Pedido" in str(pedido) 