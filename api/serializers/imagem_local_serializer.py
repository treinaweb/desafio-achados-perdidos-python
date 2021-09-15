from rest_framework import serializers


class ImagemLocalSerializer(serializers.Serializer):
    imagem_local = serializers.ImageField()