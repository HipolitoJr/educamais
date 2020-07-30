from django.contrib.auth.views import LogoutView
from django.urls import path
from administracao import views

urlpatterns = [
    path('registrar_escola/', views.RegistrarEscolaView.as_view(), name="registrar_escola"),

    path('administracao/buscas_realizadas', views.BuscasRealizadasView.as_view(), name='buscas_realizadas'),
    path('administracao/notas_alunos', views.NotasAlunosView.as_view(), name='notas_alunos'),
    path('administracao/alunos_perfil', views.AlunosPerfilView.as_view(), name='alunos_perfil'),
]
