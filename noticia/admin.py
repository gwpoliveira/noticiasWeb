from django.contrib import admin
from noticia import models
"""from .models import Autor"""

# Register your models here.
@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nome_Autor',)

@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nome_Categoria', 'descricao')