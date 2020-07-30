from django.contrib import admin

# Register your models here.
from core.models import Perfil, Prova


@admin.register(Perfil)
class TipoPerfilAdmin(admin.ModelAdmin):
    pass


@admin.register(Prova)
class TipoPerfilAdmin(admin.ModelAdmin):
    pass
