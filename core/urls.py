from django.contrib.auth.views import LogoutView
from django.urls import path

from core.views import LoginView
from core import views

urlpatterns = [
    path('registrar/', views.RegistrarUsuarioView.as_view(), name="registrar"),

    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),

    path('', views.buscar, name='buscar'),

    path('configuracoes/perfil', views.MeuPerfilView.as_view(), name='meu_perfil'),
    path('configuracoes/minhas_provas', views.MinhasProvasView.as_view(), name='minhas_provas'),
]
