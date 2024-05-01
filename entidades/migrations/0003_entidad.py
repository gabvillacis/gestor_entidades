# Generated by Django 5.0.4 on 2024-04-24 00:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_alter_tipogad_options_alter_zonal_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('ruc', models.CharField(max_length=13)),
                ('control_snap', models.BooleanField()),
                ('direccion', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=9)),
                ('correo_institucional', models.EmailField(max_length=254)),
                ('base_normativa', models.TextField(blank=True, max_length=5000, null=True)),
                ('fecha_publicacion_base_legal', models.DateField()),
                ('num_registro_oficial', models.CharField(max_length=25)),
                ('nota_aclaracion', models.TextField(blank=True, max_length=1000, null=True)),
                ('nombres_maxima_autoridad', models.CharField(max_length=100)),
                ('nombres_responsable', models.CharField(max_length=100)),
                ('correo_responsable', models.EmailField(max_length=254)),
                ('telefono_responsable', models.CharField(max_length=9)),
                ('extension_telef_responsable', models.CharField(max_length=5)),
                ('file_ordenanza', models.FileField(null=True, upload_to='')),
                ('file_registro_oficial', models.FileField(null=True, upload_to='')),
                ('file_ruc', models.FileField(null=True, upload_to='')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_ult_act', models.DateTimeField(auto_now=True)),
                ('ambito_accion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.ambitoaccion')),
                ('canton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.canton')),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.funcion')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.parroquia')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.provincia')),
                ('tipo_entidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.tipoentidad')),
                ('tipo_gad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.tipogad')),
                ('tipo_organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.tipoorganizacion')),
                ('zonal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.zonal')),
            ],
            options={
                'verbose_name': 'Entidad',
                'verbose_name_plural': 'Entidades',
                'db_table': 'ent_entidades',
            },
        ),
    ]