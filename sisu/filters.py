import django_filters
from django.contrib.auth.models import User
from django.forms import forms

from sisu.models import Curso


class CursoFilter(django_filters.FilterSet):

    nome = django_filters.ModelMultipleChoiceFilter(queryset=Curso.objects.all())

    class Meta:
        model = Curso
        fields = ['nome', 'campus', 'turno', ]