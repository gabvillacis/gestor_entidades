
# entidades/models/entidad.py
from django.db import models
from entidades.models import *

class Entidad(models.Model):
    nombre = models.CharField(max_length=250)
    ruc = models.CharField(max_length=13, unique=True)
    tipo_organizacion = models.ForeignKey(TipoOrganizacion, on_delete=models.CASCADE)
    tipo_entidad = models.ForeignKey(TipoEntidad, on_delete=models.CASCADE)
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE)
    control_snap = models.BooleanField()
    ambito_accion = models.ForeignKey(AmbitoAccion, on_delete=models.CASCADE)
    zonal = models.ForeignKey(Zonal, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    canton = models.ForeignKey(Canton, on_delete=models.CASCADE)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=10)
    correo_institucional = models.EmailField()
    tipo_gad = models.ForeignKey(TipoGad, on_delete=models.CASCADE)
    base_normativa = models.TextField(max_length=5000, blank=True, null=True)
    fecha_publicacion_base_legal = models.DateField()
    num_registro_oficial = models.CharField(max_length=25)
    nota_aclaracion = models.TextField(max_length=1000, blank=True, null=True)
    nombres_maxima_autoridad = models.CharField(max_length=100)
    nombres_responsable = models.CharField(max_length=100)
    correo_responsable = models.EmailField()
    telefono_responsable = models.CharField(max_length=10)
    extension_telef_responsable = models.CharField(max_length=5)
    file_ordenanza = models.FileField(null=True, upload_to='adjuntos/')
    file_registro_oficial = models.FileField(null=True, upload_to='adjuntos/')
    file_ruc = models.FileField(null=True, upload_to='adjuntos/')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_ult_act = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.nombre} ({self.id})'

    class Meta:
        db_table = 'ent_entidades'
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
    