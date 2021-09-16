from rest_framework import serializers
from ..models import Local, Usuario
from ..serializers import usuario_serializer, editar_usuario_serializer
from ..hateoas import Hateoas
from django.urls import reverse



class LocalSerializer(serializers.ModelSerializer):
    usuario = usuario_serializer.UsuarioSerializer()

    class Meta:
        model = Local
        fields = '__all__'

    def create(self, validated_data):
        usuario = usuario_serializer.UsuarioSerializer(data=validated_data.pop('usuario'))
        usuario.is_valid(raise_exception=True)
        usuario_criado = usuario.save()
        usuario_bd = Usuario.objects.get(email=usuario_criado)
        local = Local.objects.create(usuario_id=usuario_bd.id, **validated_data)
        return local

    def get_links(self, obj):
        links = Hateoas()
        links.add_get('self', reverse('local-list'))
        links.add_put('atualizar_local', reverse('local-detalhes', kwargs={'local_id': obj.id}))
        links.add_delete('apagar_local', reverse('local-detalhes', kwargs={'local_id': obj.id}))
        links.add_post('definir_imagem_local', reverse('imagem-local-detalhes'))
        links.add_get('listar_objetos_local', reverse('objetos-local', kwargs={'local_id': obj.id}))
        links.add_post('adicionar_objeto_local', reverse('objeto-list'))
        return links.to_array()

    # def to_representation(self, obj):
    #     usuario = Usuario.objects.get(id=obj.usuario.id)
    #     serializer_usuario = usuario_serializer.UsuarioSerializer(usuario)
    #     return {
    #         'local': {
    #             'id': obj.id,
    #             'nome': obj.nome,
    #             'endereco': obj.endereco,
    #             'contato': obj.contato,
    #             'descricao': obj.descricao,
    #             'imagem': obj.imagem_local or None
    #         },
    #         'usuario': serializer_usuario.data,
    #         'links': self.get_links(obj)
    #     }
