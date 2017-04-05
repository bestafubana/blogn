# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='post',
            name='mod_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='safetitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('DR', 'draft'), ('PB', 'published')], default='DR', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
