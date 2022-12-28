from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        exclude = ['id']

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': 'Número de CPF inválido.'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {'nome': 'O nome deve conter apenas letras.'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': 'O RG deve conter 9 números.'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': 'O número do celular deve seguir este modelo: 12 12345-1234'})
        return data
