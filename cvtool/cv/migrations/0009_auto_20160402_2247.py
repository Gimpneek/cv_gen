# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-02 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(help_text='Company worked for', max_length=256)),
                ('role', models.CharField(help_text='Role/Position held', max_length=256)),
                ('start_date', models.DateField(help_text='Date started job')),
                ('end_date', models.DateField(blank=True, help_text='Date ended job', null=True)),
                ('projects', models.ManyToManyField(related_name='projects', to='cv.Project')),
                ('responsibilities', models.ManyToManyField(related_name='responsibilities', to='cv.Responsibility')),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='cv.Tag'),
        ),
    ]
