from django.urls import path
from sisu import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('cursos/', views.CursosView.as_view(), name='cursos'),
    path('universidades/', views.UniversidadesView.as_view(), name='universidades'),
    path('comparar_cursos/', views.CompararCursosView.as_view(), name='comparar_cursos'),
]
