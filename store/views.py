from django.shortcuts import render
from rest_framework import filters, viewsets, permissions
from .models import Produto, Pedido
from .serializers import ProdutoSerializer, PedidoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters
from .filters import ProdutoFilter   # importe aqui


class IsAdminOrReadOnly(permissions.BasePermission):
    """Somente admin pode escrever; leitura liberada"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAdminOrReadOnly]
    #filter_backends = [filters.SearchFilter]
    search_fields = ["nome", "descricao"]
     # habilita busca & ordering também
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]

    filterset_class = ProdutoFilter
    ordering_fields = ["preco", "criado_em"]
    ordering = ["-criado_em"]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # cada usuário vê apenas seus próprios pedidos, admin vê todos
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(usuario=self.request.user)
 