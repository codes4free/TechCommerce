import uuid
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('nome', models.CharField(max_length=120)),
                ('descricao', models.TextField(blank=True)),
                ('preco', models.DecimalField(max_digits=10, decimal_places=2)),
                ('estoque', models.PositiveIntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10, choices=[('PENDENTE', 'Pendente'), ('PAGO', 'Pago'), ('ENVIADO', 'Enviado'), ('CONCLUIDO', 'Concluído'), ('CANCELADO', 'Cancelado')], default='PENDENTE')),
                ('total', models.DecimalField(default=0, max_digits=12, decimal_places=2)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-data_criacao'],
            },
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario', models.DecimalField(max_digits=10, decimal_places=2)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='store.Pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.Produto')),
            ],
            options={},
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('valor', models.DecimalField(max_digits=12, decimal_places=2)),
                ('metodo', models.CharField(max_length=10, choices=[('PIX', 'PIX'), ('CARTAO', 'Cartão'), ('BOLETO', 'Boleto')])),
                ('status', models.CharField(max_length=10, choices=[('PENDENTE', 'Pendente'), ('CONFIRMADO', 'Confirmado'), ('FALHOU', 'Falhou')], default='PENDENTE')),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento', to='store.Pedido')),
            ],
            options={},
        ),
    ] 