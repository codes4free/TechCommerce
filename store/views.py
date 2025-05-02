from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Produto, Pedido
from .serializers import ProdutoSerializer, PedidoSerializer


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
