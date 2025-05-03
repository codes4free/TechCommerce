# This file configures global test fixtures for the TechCommerce project using pytest.

import pytest
from rest_framework.test import APIClient

# Example fixture (customize as needed)
@pytest.fixture
def sample_data():
    return {'key': 'value'}

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def product_factory():
    from store.models import Produto
    def create_product(**kwargs):
        defaults = {
            "nome": "Produto",
            "descricao": "Default description",
            "preco": 10,
            "estoque": 10
        }
        defaults.update(kwargs)
        return Produto.objects.create(**defaults)
    return create_product 