from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Escola(models.Model):

    sigla = models.CharField(max_length=10, null=False, blank=False)
    nome = models.CharField(max_length=255, null=False, blank=False)
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='escola')

    def __str__(self):
        return "%s - %s" % (self.sigla, self.nome)
