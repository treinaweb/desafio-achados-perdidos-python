from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import objeto_dono_serializer, objeto_serializer
from ..models import Local, Objeto
from ..permissions import dono_permission


class ObjetosDonoID(APIView):
    # permission_classes = [IsAuthenticated]

    def patch(self, request, objeto_id, format=None):
        objeto = Objeto.objects.get(id=objeto_id)
        serializer = objeto_dono_serializer.ObjetoDonoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            objeto.dono_nome = serializer.validated_data["dono_nome"]
            objeto.dono_cpf = serializer.validated_data["dono_cpf"]
            objeto.entregue = True
            objeto.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)