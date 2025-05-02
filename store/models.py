# =========================
# store/models.py
# =========================
from uuid import uuid4
from decimal import Decimal
from django.conf import settings
from django.db import models

class Produto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    class Status(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        PAGO = "PAGO", "Pago"
        ENVIADO = "ENVIADO", "Enviado"
        CONCLUIDO = "CONCLUIDO", "Concluído"
        CANCELADO = "CANCELADO", "Cancelado"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pedidos")
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDENTE)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        ordering = ["-data_criacao"]

    def calcular_total(self):
        total = sum(item.subtotal for item in self.itens.all())
        self.total = total
        return total

    def save(self, *args, **kwargs):
        if self.pk:
            self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario}"


class ItemPedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self) -> Decimal:
        return self.quantidade * self.preco_unitario

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"


class Pagamento(models.Model):
    class Metodo(models.TextChoices):
        PIX = "PIX", "PIX"
        CARTAO = "CARTAO", "Cartão"
        BOLETO = "BOLETO", "Boleto"

    class Status(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        CONFIRMADO = "CONFIRMADO", "Confirmado"
        FALHOU = "FALHOU", "Falhou"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name="pagamento")
    data = models.DateTimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    metodo = models.CharField(max_length=10, choices=Metodo.choices)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PENDENTE)

    def __str__(self):
        return f"Pagamento {self.id} ({self.status})"
