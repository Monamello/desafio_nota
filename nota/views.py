from django.shortcuts import render
from rest_framework import viewsets
from .models import Nota
from .serializers import NotaSerializer


class NotaViewSet(viewsets.ModelViewSet):
    serializer_class = NotaSerializer

    def get_queryset(self):
        user = self.request.user
        return Nota.objects.filter(autor=user).all()
