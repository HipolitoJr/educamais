from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import CursoSerializer, PesoCursoSerializer, IesSerializer, CampusSerializer, PerfilSerializer
from sisu.models import Curso, PesoCurso, Ies, Campus
from core.models import Perfil


class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.order_by('id')
    serializer_class = CursoSerializer


class PesoCursoViewSet(viewsets.ModelViewSet):

    queryset = PesoCurso.objects.order_by('-id')
    serializer_class = PesoCursoSerializer


class IesViewSet(viewsets.ModelViewSet):

    queryset = Ies.objects.order_by('id')
    serializer_class = IesSerializer


class CampusViewSet(viewsets.ModelViewSet):

    queryset = Campus.objects.order_by('id')
    serializer_class = CampusSerializer


class PerfilViewSet(viewsets.ModelViewSet):

    queryset = Perfil.objects.order_by('id')
    serializer_class = PerfilSerializer