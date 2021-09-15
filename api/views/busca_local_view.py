from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import busca_local_serializer
from ..models import Local
from ..permissions import dono_permission


class BuscaLocal(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        nome = self.request.query_params.get('nome', None)
        local = Local.objects.filter(nome=nome)
        serializer = busca_local_serializer.BuscaLocalSerializer(local, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)