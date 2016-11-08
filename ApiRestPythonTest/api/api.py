from tastypie.resources import ModelResource
from api.models import FeiraLivre

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

class FeiraLivreResource(ModelResource):
    class Meta:
        queryset = FeiraLivre.objects.all()
        resource_name = 'feiraslivre'

        fields = ['ID','LONG','LAT','SETCENS','AREAP', 'CODDIST' , 'DISTRITO' , 'CODSUBPREF' , 'SUBPREFE' , 'REGIAO5' , 'REGIAO8' , 'NOME_FEIRA' ,'REGISTRO' , 'LOGRADOURO' , 'NUMERO' ,'BAIRRO' ,'REFERENCIA']
        allowed_methods = ['get', 'post', 'put', 'delete']
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'DISTRITO': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'REGIAO5' : ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'NOME_FEIRA': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'BAIRRO' : ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }

    def obj_delete(self, bundle, **kwargs):
         # get post id
         feiralivre = FeiraLivre.objects.get(registro=bundle.data.REGISTRO) 
         return super(FeiraLivreResource, self).obj_delete(bundle, user=bundle.request.user)

    def obj_create(self, bundle, request=None, **kwargs):

         bundle = super(FeiraLivreResource, self).obj_create(bundle)
    

    def obj_update(self, bundle, request = None, **kwargs):
        # update an existing row
        registro = kwargs['REGISTRO']
        try:
            bundle.obj = get_object(registro)
        except KeyError:
            raise Http404

        bundle = self.full_hydrate(bundle)
        data[registro] = bundle.obj
        return bundle


    def get_object(self, registro):
        try:
            return FeiraLivre.objects.get(registro=registro)
        except FeiraLivre.DoesNotExist:
            logger.error('FEIRALIVRE DOES NOT EXIST!')
            raise Http404