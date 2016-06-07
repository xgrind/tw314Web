# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160607_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='svc_servico',
            name='RMO_ID',
            field=models.ForeignKey(default=datetime.datetime(2016, 6, 7, 18, 9, 17, 547590, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='home.RMO_RAMO_ATIVIDADE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='atd_atendimento',
            name='ATD_DTHR_INICIO',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 7, 18, 8, 50, 178650, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cha_chamado',
            name='CHA_DT_ABERTURA',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 18, 8, 50, 175800, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='emp_empresa',
            name='EMP_DT_ABERTURA',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 18, 8, 50, 169424, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='emp_empresa',
            name='EMP_DT_ATIVACAO',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 18, 8, 50, 169510, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tck_ticket',
            name='TCK_DTHR_EMISSAO',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 7, 18, 8, 50, 177344, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usu_usuario',
            name='USU_DT_ATIVACAO',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 18, 8, 50, 172605, tzinfo=utc)),
        ),
    ]
