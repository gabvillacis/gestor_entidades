# entidades/models/catalogs.py
from django.db import models

class TipoOrganizacion(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_tipos_organizacion'
        verbose_name = 'Tipo de Organización'
        verbose_name_plural = 'Tipos de Organización'


class TipoEntidad(models.Model):
    nombre = models.CharField(max_length=75)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_tipos_entidad'
        verbose_name = 'Tipo de Entidad'
        verbose_name_plural = 'Tipos de Entidad'


class Funcion(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_tipos_funcion'
        verbose_name = 'Tipo de Función'
        verbose_name_plural = 'Tipos de Función'


class AmbitoAccion(models.Model):
    nombre = models.CharField(max_length=25)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_ambitos_accion'
        verbose_name = 'Ámbito de Acción'
        verbose_name_plural = 'Ámbitos de Acción'


class Zonal(models.Model):
    nombre = models.CharField(max_length=25)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_zonales'
        verbose_name = 'Zonal'
        verbose_name_plural = 'Zonales'


class Provincia(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'


class Canton(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_cantones'
        verbose_name = 'Cantón'
        verbose_name_plural = 'Cantones'


class Parroquia(models.Model):
    nombre = models.CharField(max_length=100)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_parroquias'
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'


class TipoGad(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_tipos_gad'
        verbose_name = 'Tipo de GAD'
        verbose_name_plural = 'Tipo de GAD'