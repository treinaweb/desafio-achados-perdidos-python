from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import objeto_serializer
from ..models import Objeto
from ..permissions import dono_objeto_permission


class ObjetoList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        objetos = Objeto.objects.filter(local__usuario=request.user.id)
        serializer = objeto_serializer.ObjetoSerializer(objetos, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = objeto_serializer.ObjetoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObjetoDetalhes(APIView):
    permission_classes = [dono_objeto_permission.DonoObjetoPermission, ]

    def get(self, request, objeto_id, format=None):
        objeto = Objeto.objects.get(id=objeto_id)
        self.check_object_permissions(request, objeto)
        serializer = objeto_serializer.ObjetoSerializer(objeto)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, objeto_id, format=None):
        objeto_antiga = Objeto.objects.get(id=objeto_id)
        self.check_object_permissions(request, objeto_antiga)
        serializer = objeto_serializer.ObjetoSerializer(objeto_antiga, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, objeto_id, format=None):
        objeto = Objeto.objects.get(id=objeto_id)
        self.check_object_permissions(request, objeto)
        objeto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
