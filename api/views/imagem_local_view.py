from rest_framework.views import APIView
from ..serializers import imagem_local_serializer
from rest_framework.response import Response
from rest_framework import status, permissions
from ..models import Local
from ..permissions import dono_permission

class ImagemLocalList(APIView):
    permission_classes = [dono_permission.DonoPermission, ]

    def post(self, request, format=None):
        local = Local.objects.get(usuario=request.user.id)
        self.check_object_permissions(request, local)
        serializer_imagem_local = imagem_local_serializer.ImagemLocalSerializer(data=request.data, context={'request': request})
        if serializer_imagem_local.is_valid():
            imagem_local = serializer_imagem_local.validated_data["imagem_local"]
            local.imagem = imagem_local
            local.save()
            return Response("Imagem cadastrada com sucesso", status=status.HTTP_200_OK)
        return Response(serializer_imagem_local.errors, status=status.HTTP_400_BAD_REQUEST)
