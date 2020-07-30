from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from administracao.models import Escola


class RegistrarEscolaView(View):
    template_name = 'registrar_escola.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        dados = request.POST
        usuario = User.objects.create_user(username=dados['inputSigla'],
                                           first_name=dados['inputSigla'],
                                           last_name=dados['inputNome'],
                                           password=dados['inputPassword'])

        escola = Escola.objects.create(sigla=dados['inputSigla'],
                                       nome=dados['inputNome'],
                                       usuario=usuario)

        return redirect('login')


class BuscasRealizadasView(View):
    template_name = 'buscas_realizadas.html'
    context = {'titulo_pagina': 'Consultas Realizadas'}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        pass


class AlunosPerfilView(View):
    template_name = 'alunos_perfil.html'
    context = {'titulo_pagina': 'Alunos por Perfil'}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        pass


class NotasAlunosView(View):
    template_name = 'notas_alunos.html'
    context = {'titulo_pagina': 'Notas por Aluno'}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        pass