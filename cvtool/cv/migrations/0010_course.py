# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20160402_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of course taken', max_length=256)),
                ('mark', models.CharField(help_text='Mark given', max_length=128)),
            ],
        ),
    ]
