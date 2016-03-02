# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 22:53


import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100, verbose_name='direcci\xf3n')),
                ('tipo', models.CharField(max_length=100, verbose_name='tipo de comercio')),
                ('descripcion', models.CharField(blank=True, max_length=256, verbose_name='descripci\xf3n')),
            ],
        ),
        migrations.CreateModel(
            name='JerarquizacionMarca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_marca', models.CharField(choices=[('premium', 'premium'), ('media', 'media'), ('economica', 'econ\xf3mica')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Jurisdiccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['region__pk', 'nombre'],
                'verbose_name': 'jurisdicci\xf3n',
                'verbose_name_plural': 'jurisdicciones',
            },
        ),
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('fecha', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Muestra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.IntegerField(verbose_name='a\xf1o')),
                ('mes', models.IntegerField(choices=[(1, 'enero'), (2, 'febrero'), (3, 'marzo'), (4, 'abril'), (5, 'mayo'), (6, 'junio'), (7, 'julio'), (8, 'agosto'), (9, 'septiembre'), (10, 'octubre'), (11, 'noviembre'), (12, 'diciembre')])),
                ('quincena', models.IntegerField(choices=[(1, 'primera'), (2, 'segunda')])),
                ('completa', models.BooleanField(default=False)),
                ('aprobada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[(b'relevador', b'relevador'), (b'coordinador_zonal', b'coordinador_zonal'), (b'coordinador_jurisdiccional', b'coordinador_jurisdiccional'), (b'coordinador_regional', b'coordinador_regional'), (b'coordinador_general', b'coordinador_general')], default=b'relevador', max_length=40)),
                ('telefono', models.CharField(blank=True, max_length=100, verbose_name='tel\xe9fono')),
                ('celular', models.CharField(blank=True, max_length=100)),
                ('enlace', models.URLField(blank=True)),
                ('notas', models.TextField(blank=True)),
                ('jurisdicciones', models.ManyToManyField(blank=True, to='relevamiento.Jurisdiccion')),
            ],
            options={
                'verbose_name_plural': 'perfiles',
            },
        ),
        migrations.CreateModel(
            name='PlanillaDeRelevamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilitada', models.BooleanField(default=False)),
                ('comercio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.Comercio')),
            ],
            options={
                'verbose_name_plural': 'planillas de relevamiento',
            },
        ),
        migrations.CreateModel(
            name='PlanillaModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('habilitada', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'planillas modelo',
            },
        ),
        migrations.CreateModel(
            name='ProductoConMarca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
        migrations.CreateModel(
            name='ProductoEnPlanilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('planilla_modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.PlanillaModelo')),
            ],
        ),
        migrations.CreateModel(
            name='ProductoGenerico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('medida', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'productos genericos',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'regi\xf3n',
                'verbose_name_plural': 'regiones',
            },
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('jurisdiccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zonas', to='relevamiento.Jurisdiccion')),
            ],
            options={
                'ordering': ['jurisdiccion__region__pk', 'jurisdiccion__nombre', 'nombre'],
            },
        ),
        migrations.AddField(
            model_name='productogenerico',
            name='rubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.Rubro'),
        ),
        migrations.AddField(
            model_name='productoenplanilla',
            name='producto_generico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.ProductoGenerico'),
        ),
        migrations.AddField(
            model_name='productoconmarca',
            name='producto_generico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.ProductoGenerico'),
        ),
        migrations.AddField(
            model_name='planillamodelo',
            name='productos',
            field=models.ManyToManyField(blank=True, through='relevamiento.ProductoEnPlanilla', to='relevamiento.ProductoGenerico'),
        ),
        migrations.AddField(
            model_name='planilladerelevamiento',
            name='planilla_modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.PlanillaModelo'),
        ),
        migrations.AddField(
            model_name='planilladerelevamiento',
            name='productos',
            field=models.ManyToManyField(blank=True, through='relevamiento.JerarquizacionMarca', to='relevamiento.ProductoConMarca'),
        ),
        migrations.AddField(
            model_name='planilladerelevamiento',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.Zona'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='regiones',
            field=models.ManyToManyField(blank=True, to='relevamiento.Region'),
        ),
        migrations.AddField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='perfil',
            name='zonas',
            field=models.ManyToManyField(blank=True, to='relevamiento.Zona'),
        ),
        migrations.AddField(
            model_name='muestra',
            name='planilla_de_relevamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.PlanillaDeRelevamiento'),
        ),
        migrations.AddField(
            model_name='muestra',
            name='relevadores',
            field=models.ManyToManyField(blank=True, to='relevamiento.Perfil'),
        ),
        migrations.AddField(
            model_name='lectura',
            name='muestra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecturas', to='relevamiento.Muestra'),
        ),
        migrations.AddField(
            model_name='lectura',
            name='producto_con_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.ProductoConMarca', verbose_name='producto'),
        ),
        migrations.AddField(
            model_name='jurisdiccion',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jurisdicciones', to='relevamiento.Region'),
        ),
        migrations.AddField(
            model_name='jerarquizacionmarca',
            name='planilla_de_relevamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.PlanillaDeRelevamiento'),
        ),
        migrations.AddField(
            model_name='jerarquizacionmarca',
            name='producto_con_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jerarquizaciones', to='relevamiento.ProductoConMarca', verbose_name='producto'),
        ),
        migrations.AddField(
            model_name='comercio',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relevamiento.Zona'),
        ),
        migrations.AlterUniqueTogether(
            name='zona',
            unique_together=set([('jurisdiccion', 'nombre')]),
        ),
        migrations.AlterUniqueTogether(
            name='productoenplanilla',
            unique_together=set([('planilla_modelo', 'orden'), ('planilla_modelo', 'producto_generico')]),
        ),
        migrations.AlterUniqueTogether(
            name='productoconmarca',
            unique_together=set([('producto_generico', 'marca')]),
        ),
        migrations.AlterUniqueTogether(
            name='planilladerelevamiento',
            unique_together=set([('planilla_modelo', 'zona', 'comercio')]),
        ),
        migrations.AlterUniqueTogether(
            name='muestra',
            unique_together=set([('planilla_de_relevamiento', 'anio', 'mes', 'quincena')]),
        ),
        migrations.AlterUniqueTogether(
            name='lectura',
            unique_together=set([('producto_con_marca', 'muestra')]),
        ),
        migrations.AlterUniqueTogether(
            name='jurisdiccion',
            unique_together=set([('region', 'nombre')]),
        ),
        migrations.AlterUniqueTogether(
            name='jerarquizacionmarca',
            unique_together=set([('planilla_de_relevamiento', 'producto_con_marca')]),
        ),
    ]
