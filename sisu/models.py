from django.db import models

class Ies(models.Model):

    codigo = models.IntegerField(blank=False, null=False)
    nome = models.CharField(max_length=255, blank=False, null=False)
    sigla = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        ordering = ('sigla',)
        verbose_name = "Ies"
        verbose_name_plural = "Ies"

    def qtde_cursos(self):
        qtde = 0
        for campus in self.campi.all():
            qtde += campus.cursos.count()
        return qtde

    def __str__(self):
        return "%s" % (self.sigla)


class Campus(models.Model):

    nome = models.CharField(max_length=255, blank=False, null=False)
    ies = models.ForeignKey(Ies, on_delete=models.CASCADE, related_name='campi')

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campi"

    def __str__(self):
        return "%s - %s" % (self.ies.sigla, self.nome.title())


class Curso(models.Model):

    codigo = models.IntegerField(blank=False, null=False)
    nome = models.TextField(max_length=255, blank=False, null=False)
    turno = models.TextField(max_length=255, blank=False, null=False)
    grau = models.TextField(max_length=255, null=False)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='cursos')

    class Meta:
        ordering = ('nome', '-campus__ies__nome',)

    def calcula_distancia_perfil(self, perfil):
        nota_perfil = self.calcula_nota_corte(perfil)
        distancia = nota_perfil - self.modalidades.all().first().nota_corte
        return "+%.2f" % distancia if distancia > 0 else "%.2f" % distancia

    def calcula_nota_corte(self, perfil):
        try:
            pesoscurso = self.pesos.order_by('disciplina')
            nota_cn = perfil.prova().nota_natureza * pesoscurso[0].peso
            nota_ch = perfil.prova().nota_humanas * pesoscurso[1].peso
            nota_lc = perfil.prova().nota_linguagens * pesoscurso[2].peso
            nota_mt = perfil.prova().nota_matematica * pesoscurso[3].peso
            nota_rd = perfil.prova().nota_redacao * pesoscurso[4].peso
            media = (nota_ch + nota_cn + nota_lc + nota_mt + nota_rd) / (pesoscurso[0].peso + pesoscurso[1].peso + pesoscurso[2].peso + pesoscurso[3].peso + pesoscurso[4].peso)
        except:
            media = 0.0
        return round(media, 2)

    def __str__(self):
        return "%s" % (self.nome)


class PesoCurso(models.Model):

    CHOICES_DISCIPLINA = (
        ('Ciências da Natureza e suas Tecnologias', 'Ciências da Natureza e suas Tecnologias'),
        ('Ciências Humanas e suas Tecnologias', 'Ciências Humanas e suas Tecnologias'),
        ('Linguagens, Códigos e suas Tecnologias', 'Linguagens, Códigos e suas Tecnologias'),
        ('Matemática e suas Tecnologias', 'Matemática e suas Tecnologias'),
        ('Redação', 'Redação'),
    )

    disciplina = models.TextField(max_length=100, choices=CHOICES_DISCIPLINA, blank=False, null=False)
    peso = models.FloatField(default=0.0, null=False, blank=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='pesos')

    def __str__(self):
        return "%s: %.2f" % (self.disciplina, self.peso)


class ModalidadeCurso(models.Model):

    tipo = models.TextField(max_length=100, blank=False, null=False)
    nota_corte = models.FloatField(null=False, blank=False)
    descricao = models.TextField(max_length=255, blank=True, null=False)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='modalidades')

    class Meta:
        verbose_name = "Modalidade Curso"
        verbose_name_plural = "Modalidades Curso"

    def __str__(self):
        return "%.2f" % (self.nota_corte)