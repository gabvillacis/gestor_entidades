from django.contrib import admin
from entidades.models import *

admin.site.site_header = 'Administrador del Catastro de Entidades'

@admin.register(TipoOrganizacion)
class TipoOrganizacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'fecha_ult_act')

@admin.register(TipoEntidad)
class TipoEntidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'fecha_ult_act')

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'fecha_ult_act')

@admin.register(AmbitoAccion)
class AmbitoAccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'fecha_ult_act')

@admin.register(Zonal)
class ZonalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'fecha_ult_act')

@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'fecha_ult_act')

@admin.register(Canton)
class CantonAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'provincia', 'fecha_registro', 'fecha_ult_act')

@admin.register(Parroquia)
class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'canton', 'fecha_registro', 'fecha_ult_act')

@admin.register(TipoGad)
class TipoGadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'fecha_ult_act')

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_organizacion', 'fecha_registro', 'fecha_ult_act')