from rest_framework import serializers
from .models import Nota


class NotaSerializer(serializers.ModelSerializer):
    autor = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    data_cricao = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Nota
        fields = '__all__'
