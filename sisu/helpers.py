from django.db.models import Count, Case, Value, When, CharField

from enem.models import Percentil
from sisu.models import Ies, Curso, Campus

BASE_CONTEXT = {}
IES_PI = [1820, 5, 756]


def get_ies():
    ies = Ies.objects.filter(codigo__in=IES_PI)
    return ies


def get_campus():
    campus = Campus.objects.filter(ies__codigo__in=IES_PI)
    return campus


def get_cursos(aggregate=False, filtro_ies=None, filtro_curso=None):

    if filtro_ies is None and filtro_curso is None:
        cursos = Curso.objects.filter(campus__ies__codigo__in=IES_PI)
    else:
        cursos = Curso.objects.all()

    if filtro_ies is not None and filtro_ies:
        cursos = cursos.filter(campus__ies__sigla=filtro_ies)
    if filtro_curso is not None and filtro_curso:
        cursos = cursos.filter(nome=filtro_curso)

    if aggregate is True:
        cursos = cursos.distinct('nome')

    return cursos


def get_percentis(*areas):
    percentis = []
    for area in areas:
        percentil = Percentil.objects.filter(area=area).annotate(faixa_tempo=Case(
            When(valor__in=range(1, 200), then=Value("de 0 a 201")),
            When(valor__in=range(201, 400), then=Value('entre 201 e 400')),
            When(valor__in=range(401, 600), then=Value('entre 401 e 600')),
            When(valor__in=range(601, 800), then=Value('entre 601 e 800')),
            default=Value('mais do que 800'),
            output_field=CharField(), )
        )
        percentis.append(percentil)

    return percentis

# 572
# 571
# 570
# 569
# 568
