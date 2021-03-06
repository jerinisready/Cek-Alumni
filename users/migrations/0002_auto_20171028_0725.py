# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 07:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cekian',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cekian',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='cekian',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cekian',
            name='passout',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(2017, django.core.validators.MinValueValidator(1980))]),
        ),
    ]
