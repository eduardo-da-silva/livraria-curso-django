from rest_framework.viewsets import ModelViewSet

from core.models import Compra
from core.serializers import CompraSerializer, CriarEditarCompraSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    # serializer_class = CompraSerializer
    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CompraSerializer
        return CriarEditarCompraSerializer
