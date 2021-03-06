# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 13:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=1000)),
                ('prep_time', models.CharField(max_length=250)),
                ('difficulty', models.CharField(max_length=50)),
                ('instructions_url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='ingredients',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_app.Recipe'),
        ),
    ]
