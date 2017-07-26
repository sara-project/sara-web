# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Área',
                'verbose_name_plural': 'Áreas',
            },
        ),
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Campus',
                'verbose_name_plural': 'Campi',
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=500)),
                ('size', models.PositiveSmallIntegerField(default=0)),
                ('year', models.PositiveSmallIntegerField(default=0)),
                ('semester', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Turma',
                'verbose_name_plural': 'Turmas',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=500)),
                ('workload', models.PositiveSmallIntegerField(default=0)),
                ('semester_number', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Disciplina',
                'verbose_name_plural': 'Disciplinas',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Dia',
                'verbose_name_plural': 'Dias',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acronym', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Requisito',
                'verbose_name_plural': 'Requisitos',
            },
        ),
        migrations.CreateModel(
            name='RequirementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo do Requisito',
                'verbose_name_plural': 'Tipos dos Requisitos',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('capacity', models.PositiveSmallIntegerField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Area')),
            ],
            options={
                'verbose_name': 'Sala',
                'verbose_name_plural': 'Salas',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo da Sala',
                'verbose_name_plural': 'Tipos das Salas',
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Class')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Day')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Room')),
            ],
            options={
                'verbose_name': 'Alocação da turma em sala',
                'verbose_name_plural': 'Alocações das turmas em salas',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Professor',
                'verbose_name_plural': 'Professores',
            },
        ),
        migrations.CreateModel(
            name='TimeInterval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Period')),
            ],
            options={
                'verbose_name': 'Intervalo de Tempo',
                'verbose_name_plural': 'Intervalos de Tempo',
            },
        ),
        migrations.AddField(
            model_name='slot',
            name='time_interval',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.TimeInterval'),
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.RoomType'),
        ),
        migrations.AddField(
            model_name='requirement',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.RequirementType'),
        ),
        migrations.AddField(
            model_name='class',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Course'),
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Teacher'),
        ),
        migrations.AddField(
            model_name='campus',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Institution'),
        ),
        migrations.AddField(
            model_name='area',
            name='campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Campus'),
        ),
        migrations.AlterUniqueTogether(
            name='slot',
            unique_together=set([('day', 'time_interval', 'room')]),
        ),
    ]
