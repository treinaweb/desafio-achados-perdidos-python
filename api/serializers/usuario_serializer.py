from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken

class UsuarioSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(required=False)
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'password', 'password_confirmation', 'token')

    # def validate_password(self, password):
    #     password_confirmation = self.initial_data["password_confirmation"]
    #     if password != password_confirmation:
    #         raise serializers.ValidationError("Senhas não combinam")
    #     return password

    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        data = {
            "refresh": str(tokens),
            "access": str(tokens.access_token)
        }
        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password')
        )
        validated_data.pop('password_confirmation', None)
        usuario = Usuario.objects.create(**validated_data)
        return usuario

    def update(self, instance, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password')
        )
        validated_data.pop('password_confirmation', None)
        instance.save(validated_data)
