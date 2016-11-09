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

