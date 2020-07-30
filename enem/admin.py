from django.contrib import admin
from enem.models import *

# Register your models here.

@admin.register(TipoPerfil)
class TipoPerfilAdmin(admin.ModelAdmin):

    list_display = ('id', 'cor_raca', 'tipo_escola', 'renda_familiar')

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):

    list_display = ('id', 'prova', 'perfil', 'frequencia', 'media', 'variancia')

@admin.register(Percentil)
class PercentilAdmin(admin.ModelAdmin):
    pass