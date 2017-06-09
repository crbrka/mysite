# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telesite', '0004_auto_20170609_1425'),
    ]

    operations = [

        migrations.CreateModel(
            name='payment_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255)),
                ('cat_fullname', models.CharField(max_length=255)),
                ('cat_createtime', models.DateTimeField(auto_now_add=True)),
                ('cat_updatetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Катеригории',
            },
        ),

    ]