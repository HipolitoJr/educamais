from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.generic.base import View

from administracao.models import Escola
from core.forms import BuscaCursosForm
from core.models import Perfil, Prova
from enem.models import TipoPerfil

@login_required
def buscar(request):
    context = {}
    busca_form = BuscaCursosForm()
    context['busca_form'] = busca_form
    return render(request, 'index.html', context)


class RegistrarUsuarioView(View):
    template_name = 'registrar.html'

    def get(self, request):
        rendas = TipoPerfil.CHOICE_RENDA
        escolas = Escola.objects.all()
        return render(request, self.template_name,
                      {'rendas': rendas,
                       'escolas': escolas})

    def post(self, request):
        dados = request.POST
        usuario = User.objects.create_user(username=dados['inputEmail'],
                                           first_name=dados['firstName'],
                                           email=dados['inputEmail'],
                                           password=dados['inputPassword'])

        tipo_perfil = TipoPerfil.objects.get(renda_familiar=dados['inputRenda'],
                                             tipo_escola=dados['inputTipoEscola'],
                                             cor_raca=dados['inputCorRaca'])

        perfil = Perfil.objects.create(tipo_perfil=tipo_perfil,
                        usuario=usuario)

        prova = Prova.objects.create(nota_humanas=dados['notaHumanas'],
                                     nota_natureza=dados['notaNatureza'],
                                     nota_linguagens=dados['notaLinguagens'],
                                     nota_matematica=dados['notaMatematica'],
                                     nota_redacao=dados['notaRedacao'],
                                     perfil=perfil,
                                     ativo=True)

        return redirect('login')


class LoginView(TemplateView):
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(request, username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            login(request, user=user)
            return redirect('buscar')

        return render(request, self.template_name)


class MeuPerfilView(View):
    context = {}
    context['titulo_pagina'] = "Meu Perfil"

    def get(self, request):
        return render(request, 'configuracoes/perfil.html', self.context)


class MinhasProvasView(View):
    context = {}
    context['titulo_pagina'] = "Minhas Provas"

    def get(self, request):
        return render(request, 'configuracoes/minhas_provas.html', self.context)