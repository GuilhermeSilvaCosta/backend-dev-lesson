# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]