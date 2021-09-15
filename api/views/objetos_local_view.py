from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import local_serializer, objeto_serializer
from ..models import Local, Objeto
from ..permissions import dono_permission


class ObjetosLocalID(APIView):
    def get(self, request, local_id, format=None):
        objetos = Objeto.objects.filter(local_id=local_id)
        serializer = objeto_serializer.ObjetoSerializer(objetos, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)