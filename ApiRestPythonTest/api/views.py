from django.shortcuts import render
from api.models import FeiraLivre
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import renderers
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet
from rest_framework import generics
import django_filters
from django.core.exceptions import ObjectDoesNotExist

import logging

# Create your views here.

logger = logging.getLogger(__name__)

class FeiraLivreViewSet(viewsets.ViewSet):

    #filter_backends = (filters.SearchFilter,)
    #search_fields  = ('DISTRITO', 'REGIAO5', 'NOME_FEIRA', 'BAIRRO' )

    """
    Listar Todas as Feiras Livres
    """
    def list(self, request):
        pass
        #feiras = FeiraLivre.objects.all()
        #serializer = FeiraSerializer(feiras, many=True)
        #return Response(serializer.data)

    """
    Criar nova feira Livre
    """
    def create(self, request):
        pass
        #serializer = SnippetSerializer(data=request.data)
        #if serializer.is_valid():
        #    serializer.save()
        #    return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """
    Atualiza feira Livre
    """
    def update(self, request, registro):
        pass
        """feira = self.get_object(registro)
        serializer = FeiraSerializer(feira, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


        logger.error('BAD REQUEST!')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

    """
    remove feira Livre
    """
    def destroy(self, request, registro):
        feira = get_object(self,registro)
        feira.delete()
        logger.warn('FEIRALIVRE REMOVED!')
        return Response(status=status.HTTP_204_NO_CONTENT)

    """
    obtém feira livre através do registro
    """
    def get_object(self, registro):
        try:
            return FeiraLivre.objects.get(registro=registro)
        except FeiraLivre.DoesNotExist:
            logger.error('FEIRALIVRE DOES NOT EXIST!')
            raise Http404
