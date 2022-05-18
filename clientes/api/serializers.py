from rest_framework import serializers
from ..models import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'data_nascimento', 'endereco', 'telefone']

