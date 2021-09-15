from rest_framework.views import APIView
from ..serializers import imagem_objeto_serializer
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import Objeto
from ..permissions import dono_permission

class ImagemObjetoList(APIView):
    permission_classes = [dono_permission.DonoPermission, ]

    def post(self, request, objeto_id, format=None):
        objeto = Objeto.objects.get(id=objeto_id)
        self.check_object_permissions(request, objeto)
        serializer_imagem_objeto = imagem_objeto_serializer.ImagemObjetoSerializer(data=request.data, context={'request': request})
        if serializer_imagem_objeto.is_valid():
            imagem_objeto = serializer_imagem_objeto.validated_data["imagem_objeto"]
            objeto.imagem_objeto = imagem_objeto
            objeto.save()
            return Response("Imagem cadastrada com sucesso", status=status.HTTP_200_OK)
        return Response(serializer_imagem_objeto.errors, status=status.HTTP_400_BAD_REQUEST)
