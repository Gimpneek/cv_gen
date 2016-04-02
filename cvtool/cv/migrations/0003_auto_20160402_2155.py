# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 21:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='skill',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='cv.Skill'),
        ),
    ]
