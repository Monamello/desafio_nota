from rest_framework import viewsets, permissions
from .models import Nota
from .serializers import NotaSerializer


class NotaViewSet(viewsets.ModelViewSet):
    serializer_class = NotaSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Nota.objects.filter(autor=user).all()
