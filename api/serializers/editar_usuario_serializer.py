from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken

class EditarUsuarioSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=False)
    class Meta:
        model = Usuario
        fields = ('nome', 'email')


    # def update(self, instance, validated_data):
    #     validated_data['password'] = make_password(
    #         validated_data.get('password')
    #     )
    #     validated_data.pop('password_confirmation', None)
    #     instance.save(validated_data)
