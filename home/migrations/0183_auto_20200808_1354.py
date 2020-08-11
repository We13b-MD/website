# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-08 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0182_auto_20200807_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectskill',
            name='skill',
            field=models.CharField(max_length=100, validators=[home.models.skill_is_valid], verbose_name='Skill name'),
        ),
    ]