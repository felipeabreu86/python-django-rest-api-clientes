from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']