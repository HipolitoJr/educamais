from django.contrib import admin

# Register your models here.
from sisu.models import Curso, Ies, Campus, ModalidadeCurso, PesoCurso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):

    list_display = ['codigo', 'nome', 'campus', 'turno', 'grau']


@admin.register(Ies)
class IesAdmin(admin.ModelAdmin):

    list_display = ['sigla', 'nome',]


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):

    list_display = ['nome', 'ies',]


@admin.register(ModalidadeCurso)
class ModalidadeCursoAdmin(admin.ModelAdmin):

    list_display = ['tipo', 'nota_corte', 'curso']


@admin.register(PesoCurso)
class PesoCursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'disciplina', 'peso', 'curso']