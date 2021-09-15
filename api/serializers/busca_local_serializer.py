from rest_framework import serializers
from ..models import Local, Usuario
from ..serializers import usuario_serializer
from ..hateoas import Hateoas
from django.urls import reverse



class BuscaLocalSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Local
        exclude = ('usuario', )

    def get_links(self, obj):
        links = Hateoas()
        links.add_get('listar_objetos_local', reverse('objetos-local', kwargs={'local_id': obj.id}))
        return links.to_array()
