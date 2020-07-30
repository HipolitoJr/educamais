from django.urls import path
from enem import views

urlpatterns = [
    path('notas_prova/', views.NotasProvaView.as_view(), name='notas_prova'),
    path('notas_perfil/', views.NotasPerfilView.as_view(), name='notas_perfil'),
    path('comparar_perfis/', views.CompararPerfisView.as_view(), name='comparar_perfis'),
]
