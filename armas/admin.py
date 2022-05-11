from django.contrib import admin
from .models import Calibre, Municao, Arma, ObjetoTipo, Objeto


# Register your models here.
@admin.register(Calibre)
class CalibreAdmin(admin.ModelAdmin):
    list_display = ['desc_calibre']


@admin.register(Municao)
class MunicaoAdmin(admin.ModelAdmin):
    list_display = ['modelo_municao', 'marca_municao']


@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ['modelo_armamento', 'marca_armamento']


@admin.register(ObjetoTipo)
class ObjetoTipoAdmin(admin.ModelAdmin):
    list_display = ['tipo_de_objeto']


@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ['objeto_tipo']
