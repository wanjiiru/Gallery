# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myGallery', '0002_auto_20180712_1428'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='iamge_category',
            new_name='image_category',
        ),
    ]
