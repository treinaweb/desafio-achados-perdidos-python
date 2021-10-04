from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import local_serializer, usuario_serializer, editar_local_serializer
from ..models import Local
from ..permissions import dono_permission


class LocalList(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        locais = Local.objects.get(usuario=request.user.id)
        serializer = local_serializer.LocalSerializer(locais, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = local_serializer.LocalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        local_antigo = Local.objects.get(usuario=request.user.id)
        self.check_object_permissions(request, local_antigo)
        serializer = editar_local_serializer.EditarLocalSerializer(instance=local_antigo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, local_id, format=None):
        local = Local.objects.get(id=local_id)
        self.check_object_permissions(request, local)
        local.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


