from django.contrib import admin
from .models import Cursos, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('categoria',)

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('titulo','data_criacao','categoria', 'descricao', 'imagem',)