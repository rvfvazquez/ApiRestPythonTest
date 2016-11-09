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
from tastypie.authorization import DjangoAuthorization
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from tastypie.throttle import BaseThrottle

import logging

class FeiraLivreResource(ModelResource):
    class Meta:
        queryset = FeiraLivre.objects.all()
        resource_name = 'feiraslivre'
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

        throttle = BaseThrottle(throttle_at=100)

        fields = ['ID','LONG','LAT','SETCENS','AREAP', 'CODDIST' , 'DISTRITO' , 'CODSUBPREF' , 'SUBPREFE' , 'REGIAO5' , 'REGIAO8' , 'NOME_FEIRA' ,'REGISTRO' , 'LOGRADOURO' , 'NUMERO' ,'BAIRRO' ,'REFERENCIA']
        allowed_methods = ['get', 'post', 'put', 'delete']
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'DISTRITO': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'REGIAO5' : ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'NOME_FEIRA': ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
            'BAIRRO' : ['exact', 'range', 'gt', 'gte', 'lt', 'lte'],
        }

    def obj_delete(self, bundle, **kwargs):
        """
        Remove objeto individual (feiralivre) através da PK (registro) (HTTP DELETE)
        """
        feiralivre = FeiraLivre.objects.get(REGISTRO = kwargs['pk']) 
        feiralivre.delete()

    def obj_create(self, bundle, request=None, **kwargs):
        """
        Cria objeto individual (feiralivre) através da PK (registro)(HTTP POST)
        """
        bundle = super(FeiraLivreResource, self).obj_create(bundle)

    def obj_update(self, bundle, request = None, **kwargs):
        """
        Atualza objeto individual (feiralivre) através da PK (registro)(HTTP PUT)
        """
        try:
            feiralivre = FeiraLivre.objects.get(REGISTRO = kwargs['pk']) 
            feiralivre.REFERENCIA =    bundle.data["REFERENCIA"]
            feiralivre.save()
            bundle.obj = feiralivre

            lookup_kwargs = kwargs.copy()
            setattr(bundle.obj,self._meta.detail_uri_name, bundle.data[self._meta.detail_uri_name])
            
            for key in kwargs.keys():
                if key == 'pk' or key == 'REGISTRO' or key == 'ID':
                    continue
                elif getattr(bundle.obj, key, NOT_AVAILABLE) is not NOT_AVAILABLE:
                    lookup_kwargs[key] = getattr(bundle.obj, key)
                else:
                    del lookup_kwargs[key] 
            
        except KeyError:
            raise Http404

        bundle = self.full_hydrate(bundle)
        data[bundle.obj.ID] = bundle.obj
        return bundle

    
    def obj_get(self, request=None, **kwargs):
        """
        Retorna um objeto individual (feiralivre) através da PK (registro) (HTTP GET)
        """
        obj = FeiraLivre.objects.get(REGISTRO = kwargs['pk'])
        return obj


    """def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'No data provided.'}
        errors = {}
        if bundle.data.get('REGISTRO', '') == '':
            errors['REGISTRO'] = 'REGISTRO cannot be empty'
        if bundle.data.get('NOME_FEIRA', '') == '':
            errors['NOME_FEIRA'] = 'NOME_FEIRA cannot be empty'
        return errors
"""