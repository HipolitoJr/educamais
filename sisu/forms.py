from django import forms
from sisu.models import Curso


class CursoForm(forms.ModelForm):

    nome = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Curso
        fields = ('nome', 'campus', 'turno', )