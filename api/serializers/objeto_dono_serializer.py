from rest_framework import serializers


class ObjetoDonoSerializer(serializers.Serializer):
    dono_nome = serializers.CharField()
    dono_cpf = serializers.CharField()
