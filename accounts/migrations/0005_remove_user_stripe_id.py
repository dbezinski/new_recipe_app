# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 11:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20171007_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='stripe_id',
        ),
    ]
