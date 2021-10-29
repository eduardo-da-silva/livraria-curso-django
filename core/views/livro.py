from rest_framework.viewsets import ModelViewSet

from core.models import Livro
from core.serializers import LivroSerializer, LivroDetailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    # serializer_class = LivroSerializer
    def get_serializer_class(self):
        if self.action == "list":
            return LivroDetailSerializer
        if self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer
