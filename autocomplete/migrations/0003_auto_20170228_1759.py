# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autocomplete', '0002_auto_20170228_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]