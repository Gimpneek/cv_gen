# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 22:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20160402_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='freshness',
            field=models.SmallIntegerField(choices=[(1, 'Not Current Practice'), (2, 'Out of Date'), (3, 'On Way Out'), (4, 'Current Practice'), (5, 'Not Widely Adopted Yet')], default=4, help_text='Is skill current practice?'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.SmallIntegerField(choices=[(1, 'No Proficiency'), (2, 'Basic Understanding'), (3, 'Working Knowledge'), (4, 'Advanced Knowledge'), (5, 'Expert Knowledge')], default=2, help_text='Proficiency of skill'),
        ),
    ]
