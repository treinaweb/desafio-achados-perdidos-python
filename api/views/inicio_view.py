from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..hateoas import Hateoas
from django.urls import reverse

class Inicio(APIView):
    def get(self, request, format=None):
        links = Hateoas()
        links.add_post('criar_local', reverse('local-list'))
        links.add_get('buscar_locais', reverse('busca-local-list'))
        return Response({"links": links.to_array()}, status=status_http.HTTP_200_OK)
