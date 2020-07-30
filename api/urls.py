from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'ies', views.IesViewSet)
router.register(r'campus', views.CampusViewSet)
router.register(r'cursos', views.CursoViewSet)
router.register(r'perfis', views.PerfilViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
