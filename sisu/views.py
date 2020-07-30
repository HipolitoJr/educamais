from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Max, Case, When, Value, CharField
from django.shortcuts import render, redirect
from django.views import View

from core.forms import BuscaCursosForm
from enem.models import Percentil
from sisu.forms import CursoForm
from sisu.helpers import get_campus, get_cursos, get_percentis
from django.contrib.auth.models import User
from django.shortcuts import render
from sisu.models import Curso, ModalidadeCurso, Ies
from .filters import CursoFilter
from django.db.models import Sum

class DashboardView(View):
    context = {}
    context['titulo_pagina'] = "Dashboard"

    def get(self, request):
        form = BuscaCursosForm(request.GET)
        self.context['form'] = request.GET.dict

        cursos_list = get_cursos(filtro_curso= form['curso'].value(),
                                 filtro_ies=form['universidade'].value())

        self.context['maior_nota'] = self.maior_nota(cursos_list)
        self.context['percentual_acima'] = self.percentual_acima(cursos_list)
        self.context['qtde_classificacoes'] = self.qtde_classificacoes(cursos_list)
        self.context['melhor_pontuacao'], self.context['melhor_curso'] = self.melhor_pontuacao(cursos_list)
        self.context['cursos'] = cursos_list

        return render(request, 'dashboard.html', self.context)

    def percentual_acima(self, cursos):
        modalidades = ModalidadeCurso.objects.filter(id__in=cursos.values('modalidades'))
        notas_acima = self.qtde_classificacoes(cursos)

        cursos = modalidades.values('nota_corte').filter(tipo='Ampla Concorrência')
        notas_total = cursos.count()

        percentual = "%.2f" % ((notas_acima * 100) / notas_total)
        return percentual

    def qtde_classificacoes(self, cursos):
        modalidades = ModalidadeCurso.objects.filter(id__in=cursos.values('modalidades'))
        cursos = modalidades.values('nota_corte').filter(tipo='Ampla Concorrência')
        notas_acima = 0

        for curso in cursos:
            if float(self.request.user.perfil.media_simples()) > curso['nota_corte']:
                notas_acima += 1

        return notas_acima

    def maior_nota(self, cursos):
        modalidades = ModalidadeCurso.objects.filter(id__in=cursos.values('modalidades'))
        maior_nota = modalidades.filter(tipo='Ampla Concorrência').order_by('-nota_corte').first()

        return maior_nota

    def melhor_pontuacao(self, cursos):
        melhor_nota = 0
        melhor_curso = None
        for curso in cursos.all():
            nota_corte = curso.calcula_nota_corte(self.request.user.perfil)
            if nota_corte > melhor_nota:
                melhor_nota, melhor_curso = nota_corte, curso
        return melhor_nota, melhor_curso


class CursosView(View):
    context = {}
    context['titulo_pagina'] = "Cursos"

    def get(self, request):
        cursos_list = get_cursos()
        self.context['cursos'] = cursos_list

        perc = get_percentis(572, 571)
        print('perc:', perc)

        percentis = Percentil.objects.filter(area=572).annotate(faixa_tempo=Case(
            When(valor__in=range(1, 200), then=Value("de 0 a 201")),
            When(valor__in=range(201, 400), then=Value('entre 201 e 400')),
            When(valor__in=range(401, 600), then=Value('entre 401 e 600')),
            When(valor__in=range(601, 800), then=Value('entre 601 e 800')),
            default=Value('mais do que 800'),
            output_field=CharField(), )
        )
        percentis = percentis.values('faixa_tempo').annotate(Sum('frequencia')).order_by('faixa_tempo')
        self.context['percentis'] = percentis
        self.context['frequencias'] = [percentil['frequencia__sum'] for percentil in percentis]
        self.context['faixas_tempo'] = [percentil['faixa_tempo'] for percentil in percentis]

        return render(request, 'cursos.html', self.context)


class UniversidadesView(View):
    context = {}
    context['titulo_pagina'] = "Universidades"

    def get(self, request):
        universidades = Ies.objects.all()
        self.context['universidades'] = universidades

        return render(request, 'universidades.html', self.context)


class CompararCursosView(View):
    context = {}
    context['titulo_pagina'] = "Comparar Cursos"

    def get(self, request):
        return render(request, 'comparar_cursos.html', self.context)
