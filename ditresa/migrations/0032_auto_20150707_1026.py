# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ditresa', '0031_auto_20150706_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='natal',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 7, 15, 26, 39, 212618, tzinfo=utc), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='jupiter',
            field=models.CharField(blank=True, null=True, verbose_name='Jupiter', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='mars',
            field=models.CharField(blank=True, null=True, verbose_name='Mars', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='mercury',
            field=models.CharField(blank=True, null=True, verbose_name='Mercury', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='moon',
            field=models.CharField(blank=True, null=True, verbose_name='Moon', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='neptun',
            field=models.CharField(blank=True, null=True, verbose_name='Neptun', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='pluto',
            field=models.CharField(blank=True, null=True, verbose_name='Pluto', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='saturn',
            field=models.CharField(blank=True, null=True, verbose_name='Saturn', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='sun',
            field=models.CharField(blank=True, null=True, verbose_name='Sun', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 7, 15, 26, 39, 213617, tzinfo=utc), verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='natal',
            name='uran',
            field=models.CharField(blank=True, null=True, verbose_name='Uran', max_length=20),
        ),
        migrations.AlterField(
            model_name='natal',
            name='venus',
            field=models.CharField(blank=True, null=True, verbose_name='Venus', max_length=20),
        ),
    ]
