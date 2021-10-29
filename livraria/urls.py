from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r"autores", views.AutorViewSet)
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"editoras", views.EditoraViewSet)
router.register(r"livros", views.LivroViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teste/", views.teste),
    path("pag2/", views.teste2),
    path("categorias-class/", views.CategoriaView.as_view()),
    path("categorias-class/<int:id>/", views.CategoriaView.as_view()),
    path("categorias-apiview/", views.CategoriasList.as_view()),
    path("categorias-apiview/<int:id>/", views.CategoriaDetail.as_view()),
    path("categorias-generic/", views.CategroriasListGeneric.as_view()),
    path("categorias-generic/<int:id>/", views.CategoriaDetailGeneric.as_view()),
    path("", include(router.urls)),
]
