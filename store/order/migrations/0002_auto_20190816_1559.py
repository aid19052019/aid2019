# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-08-16 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='close_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='订单关闭时间'),
        ),
    ]
