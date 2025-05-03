import os, django, random, decimal
from faker import Faker

# Add the project root to sys.path so that 'techcommerce' can be imported
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techcommerce.settings")
django.setup()

from store.models import Produto

fake = Faker("pt_BR")
if os.getenv("ALLOW_SEED") != "1":
    print("🚫  ALLOW_SEED not set — aborting seed")
    sys.exit(0)

Produto.objects.all().delete()

for _ in range(20):
    Produto.objects.create(
        nome=fake.word().title(),
        descricao=fake.sentence(nb_words=8),
        preco=decimal.Decimal(random.randint(10, 500)),
        estoque=random.randint(5, 50),
    )

print("Seed completo – 20 produtos inseridos.")
