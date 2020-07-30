from django.db import models
from statistics import *

# Create your models here.

class TipoPerfil(models.Model):

    CHOICE_COR_RACA = (
        ('0', 'Não declarado',),
        ('1', 'Branca',),
        ('2', 'Preta',),
        ('3', 'Parda',),
        ('4', 'Amarela',),
        ('5', 'Indígena',),
    )

    CHOICE_ESCOLA = (
        ('1', 'Não informada',),
        ('2', 'Pública',),
        ('3', 'Privada',),
        ('4', 'Exterior',),
    )

    CHOICE_RENDA = (
        ('A', 'Nenhuma'),
        ('B', 'Até R$937,00'),
        ('C', 'de R$937,01 até R$1.405,50'),
        ('D', 'de R$1.405,51 até R$1.874,00'),
        ('E', 'de R$1.874,01 até R$2.342,50'),
        ('F', 'de R$2.342,51 até R$2.811,00'),
        ('G', 'de R$2.811,01 até R$3.748,00'),
        ('H', 'de R$3.748,01 até R$4.685,00'),
        ('I', 'de R$4.685,01 até R$5.622,00'),
        ('J', 'de R$5.622,01 até R$6.559,00'),
        ('K', 'de R$6.559,01 até R$7.496,00'),
        ('L', 'de R$7.496,01 até R$8.433,00'),
        ('M', 'de R$8.433,01 até R$9.370,00'),
        ('N', 'de R$9.370,01 até R$11.244,00'),
        ('O', 'de R$11.244,01 até R$14.055,00'),
        ('P', 'de R$14.055,01 até R$18.740,00'),
        ('Q', 'Acima de R$18.740,01'),
    )

    cor_raca = models.CharField(max_length=20, choices=CHOICE_COR_RACA, null=False)
    tipo_escola = models.CharField(max_length=50, choices=CHOICE_ESCOLA, null=False)
    renda_familiar = models.CharField(max_length=255, choices=CHOICE_RENDA, null=False)

    class Meta:
        verbose_name = "Tipo de Perfil"
        verbose_name_plural = "Tipos de Perfis"

    def media_perfil(self):
        notas = self.notas()
        media = median(notas)
        return media

    def notas(self):
        return [round(area.media, 2) for area in self.areas.all()]

    def __str__(self):
        return "%s%s%s" % (self.cor_raca, self.renda_familiar, self.tipo_escola)


class Area(models.Model):

    CHOICE_PROVAS = (
        ('LC', 'Linguagens e códigos'),
        ('MT', 'Matématica e suas Tecnologias'),
        ('CH', 'Ciências Humanas'),
        ('CN', 'Ciências da Natureza'),
        ('REDACAO', 'Redação')
    )

    prova = models.TextField(max_length=255, choices=CHOICE_PROVAS, null=False)
    frequencia = models.IntegerField()
    media = models.FloatField(default=0.00, null=False)
    variancia = models.FloatField(default=0.00, null=False)

    perfil = models.ForeignKey(TipoPerfil, on_delete=models.CASCADE, related_name='areas')

    def __str__(self):
        return "%.2f" % (self.media)


class Percentil(models.Model):

    valor = models.IntegerField(null=False)
    frequencia = models.IntegerField(null=False)
    media = models.FloatField(default=0.00, null=False)

    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='percentis')

    class Meta:
        verbose_name_plural = "Percentis"




