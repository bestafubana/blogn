# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170402_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='safetitle',
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='mod_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
