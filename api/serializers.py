from rest_framework import serializers
from sisu.models import Curso, PesoCurso, ModalidadeCurso, Ies, Campus
from core.models import Perfil


class PesoCursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PesoCurso
        fields = ('disciplina', 'peso', )


class ModalidadeCursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModalidadeCurso
        fields = ('tipo', 'nota_corte', 'descricao', )


class CursoSerializer(serializers.ModelSerializer):

    # pesos = PesoCursoSerializer(many=True, read_only=True)
    modalidades = ModalidadeCursoSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = ('id', 'codigo', 'nome', 'modalidades', )


class CampusSerializer(serializers.ModelSerializer):

    cursos = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nome'
    )

    ies = serializers.SlugRelatedField(
        read_only=True,
        slug_field='sigla'
    )

    class Meta:
        model = Campus
        fields = ('id', 'nome', 'ies', 'cursos', )


class IesSerializer(serializers.ModelSerializer):

    campi = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='nome'
    )

    class Meta:
        model = Ies
        fields = ('id', 'codigo', 'sigla', 'nome', 'campi', )


class PerfilSerializer(serializers.ModelSerializer):

    usuario = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Perfil
        fields = ('usuario',
                  'renda',
                  'cor_raca',
                  'tipo_escola',
                  'nota_natureza', 'nota_humanas',
                  'nota_matematica', 'nota_linguagens',
                  'nota_redacao',
                  )