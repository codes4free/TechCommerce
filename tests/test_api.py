import pytest
pytestmark = pytest.mark.django_db

from decimal import Decimal


def test_product_list(api_client, product_factory):
    product_factory()
    res = api_client.get("/api/produtos/?page_size=3")
    assert res.status_code == 200
    assert len(res.data) <= 3


def test_create_and_get_order(api_client, product_factory, django_user_model):
    user = django_user_model.objects.create_user(username="foo", password="pass")
    api_client.force_authenticate(user=user)
    prod = product_factory(preco=30)
    payload = {"itens": [{"produto_id": str(prod.id), "quantidade": 2}]}
    # create
    res = api_client.post("/api/pedidos/", payload, format="json")
    assert res.status_code == 201
    order_id = res.data["id"]
    assert Decimal(res.data["total"]) == Decimal("60")
    # retrieve
    res2 = api_client.get(f"/api/pedidos/{order_id}/")
    assert res2.status_code == 200
    assert res2.data["id"] == order_id 