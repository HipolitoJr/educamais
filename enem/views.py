from django.core.paginator import Paginator
from django.db.models import When, Case, Value, CharField, Sum
from django.shortcuts import render
from django.views import View

from enem.models import TipoPerfil, Percentil


class NotasPerfilView(View):
    context = {}
    context['titulo_pagina'] = "Notas médias por Perfil"

    def get(self, request):
        perfis_list = TipoPerfil.objects.all()
        self.context['perfis'] = perfis_list

        meu_perfil = TipoPerfil.objects.get(cor_raca=request.user.perfil.tipo_perfil.cor_raca,
                                            renda_familiar=request.user.perfil.tipo_perfil.renda_familiar,
                                            tipo_escola=request.user.perfil.tipo_perfil.tipo_escola)
        self.context['meu_perfil'] = meu_perfil

        return render(request, 'medias_perfis.html', self.context)


class NotasProvaView(View):
    context = {}
    context['titulo_pagina'] = "Notas por Prova"

    def get(self, request):
        percentis_total = {}
        for area in request.user.perfil.tipo_perfil.areas.all():
            percentis = self.calcula_percentis(area)
            frequencias = [percentil['frequencia__sum'] for percentil in percentis]
            total = sum(frequencias)
            frequencias = [round(item/total, 1)*100 for item in frequencias]
            percentis_total[area.prova.lower()] = frequencias

        self.context['percentis'] = percentis_total

        return render(request, 'notas_prova.html', self.context)

    def calcula_percentis(self, area):
        percentis = Percentil.objects.filter(area=area).annotate(faixa_tempo=Case(
            When(valor__in=range(1, 300), then=Value("ate 300")),
            When(valor__in=range(301, 400), then=Value('entre 201 e 400')),
            When(valor__in=range(401, 500), then=Value('entre 401 e 500')),
            When(valor__in=range(501, 600), then=Value('entre 501 e 600')),
            When(valor__in=range(601, 700), then=Value('entre 601 e 700')),
            When(valor__in=range(701, 800), then=Value('entre 701 e 800')),
            When(valor__in=range(801, 900), then=Value('entre 801 e 900')),
            default=Value('acima de 800'),
            output_field=CharField(), )
        )

        return percentis.values('faixa_tempo').annotate(Sum('frequencia')).order_by('faixa_tempo')

class CompararPerfisView(View):
    context = {}
    context['titulo_pagina'] = 'Comparar Perfis'

    def get(self, request):
        return render(request, 'comparar_perfis.html', self.context)