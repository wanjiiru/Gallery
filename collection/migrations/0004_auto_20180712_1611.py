# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20180712_1608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AddField(
            model_name='category',
            name='cat',
            field=models.CharField(choices=[('Food', 'Food'), ('Cars', 'Cars'), ('Shoes', 'Shoes'), ('Quotes', 'Quotes')], default=1, max_length=255),
            preserve_default=False,
        ),
    ]
