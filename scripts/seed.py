import os, django, random, decimal
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techcommerce.settings")
django.setup()

from store.models import Produto  # ajuste path conforme app

fake = Faker("pt_BR")
Produto.objects.all().delete()

for _ in range(20):
    Produto.objects.create(
        nome=fake.word().title(),
        descricao=fake.sentence(nb_words=8),
        preco=decimal.Decimal(random.randint(10, 500)),
        estoque=random.randint(5, 50),
    )

print("Seed completo – 20 produtos inseridos.")
