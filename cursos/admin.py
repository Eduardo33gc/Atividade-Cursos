from django.contrib import admin
from .models import Alimentos, Apicultura, Informatica

# Register your models here.

@admin.register(Alimentos)
class AlimentosAdmin(admin.ModelAdmin):
    list_display=('titulo','texto','data_criacao','imagem')

@admin.register(Apicultura)
class ApiculturaAdmin(admin.ModelAdmin):
    list_display=('titulo','texto','data_criacao','imagem')

@admin.register(Informatica)
class InformaticaAdmin(admin.ModelAdmin):
    list_display=('titulo','texto','data_criacao','imagem')




