from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from accounts.serializers import UserSerializer
from .permissions import IsNotAuthenticated


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsNotAuthenticated,)
