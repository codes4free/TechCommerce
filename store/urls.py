from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet, PedidoViewSet

router = DefaultRouter()
router.register("produtos", ProdutoViewSet)
router.register("pedidos", PedidoViewSet)

urlpatterns = router.urls
