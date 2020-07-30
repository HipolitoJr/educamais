from django.contrib.auth.models import User
from django.db import models

from administracao.models import Escola
from enem.models import TipoPerfil

class Perfil(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    tipo_perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE, related_name='perfis')
    escola = models.ForeignKey(Escola, null=True, on_delete=models.CASCADE, related_name='alunos')

    def prova(self):
        return self.provas.filter(ativo=True).first()

    def notas(self):
        return [self.prova().nota_linguagens, self.prova().nota_matematica, self.prova().nota_redacao, self.prova().nota_humanas, self.prova().nota_natureza]

    def media_simples(self):
        media = (self.prova().nota_humanas + self.prova().nota_linguagens +
                 self.prova().nota_matematica + self.prova().nota_natureza +
                 self.prova().nota_redacao) / 5
        return "%.2f" % media


class Prova(models.Model):
    nota_natureza = models.FloatField(default=0.0, null=False)
    nota_humanas = models.FloatField(default=0.0, null=False)
    nota_matematica = models.FloatField(default=0.0, null=False)
    nota_linguagens = models.FloatField(default=0.0, null=False)
    nota_redacao = models.FloatField(default=0.0, null=False)

    ativo = models.BooleanField(default=False)
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='provas')
