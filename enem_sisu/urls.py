"""enem_sisu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from sisu import views as core_views
from core.views import LoginView

urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('administracao.urls')),
    path('', include('core.urls')),
    path('sisu/', include('sisu.urls')),
    path('enem/', include('enem.urls')),
    path('admin/', admin.site.urls),
    path('select2/',  include('django_select2.urls')),

    # path('', core_views.index, name='index'),
    # path('cursos/', core_views.cursos, name='cursos'),
    # path('dados/', core_views.dados, name='dados'),
    # path('dados_tabelas/', core_views.dados_tabelas, name='dados_tabelas'),
    # path('dados_graficos/', core_views.dados_graficos, name='dados_graficos'),
    # path('registrar/', core_views.registrar, name='registrar'),
    # path('registrar-perfil/', core_views.registrar_perfil, name='registrar_perfil'),
    # path('consulta/', core_views.consulta, name='consulta')
]
