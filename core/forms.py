from django import forms
from django.forms import Select

from sisu.helpers import get_cursos
from sisu.models import Curso, Ies


class BuscaCursosForm(forms.Form):

    universidade = forms.ModelChoiceField(
        label = "Selecione uma universidade",
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Ies.objects.all().distinct('sigla')
    )

    curso = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
        queryset =Curso.objects.all().distinct('nome')
    )

