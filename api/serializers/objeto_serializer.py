from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Objeto, Local
from ..serializers import local_serializer
from ..hateoas import Hateoas


class ObjetoSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    entregue = serializers.BooleanField(read_only=True)

    class Meta:
        model = Objeto
        exclude = ('local', 'dono_nome', 'dono_cpf', 'imagem')

    def create(self, validated_data):
        usuario = self.context['request'].user.id
        local = Local.objects.get(usuario_id=usuario)
        objeto = Objeto.objects.create(local_id=local.id, **validated_data)

        return objeto

    def get_links(self, obj):
        links = Hateoas()
        links.add_get('self', reverse('objeto-detalhes', kwargs={'objeto_id': obj.id}))
        links.add_put('atualizar_objeto', reverse('objeto-detalhes', kwargs={'objeto_id': obj.id}))
        links.add_delete('apagar_objeto', reverse('objeto-detalhes', kwargs={'objeto_id': obj.id}))
        links.add_post('definir_imagem_objeto', reverse('imagem-objeto-detalhes', kwargs={'objeto_id': obj.id}))
        links.add_post('definir_dono_objeto', reverse('objeto-dono-detalhes', kwargs={'objeto_id': obj.id}))
        return links.to_array()